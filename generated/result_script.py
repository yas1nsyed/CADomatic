import FreeCAD as App
import Part
from FreeCAD import Vector, Placement, Rotation
import math

# Create a new document
DOC_NAME = "Screw"
DOC = App.newDocument(DOC_NAME)
App.setActiveDocument(DOC.Name)

# --- Dimensions ---
# Screw Head Dimensions (Hexagonal)
head_across_flats = 10.0  # Distance across the flats of the hex head
head_height = 5.0

# Screw Shank Dimensions (Nominal Major Diameter)
shank_major_diameter = 6.0  # e.g., for M6 screw
shank_length = 25.0

# Thread Dimensions (for a V-groove cut, approximating a metric thread)
pitch = 1.0  # Distance between threads
thread_depth = 0.54127 * pitch 
thread_half_angle_rad = math.radians(30) # Half angle for a 60 degree V-thread

# --- Create Screw Head (Hexagonal) ---
hex_radius_to_vertex = (head_across_flats / 2.0) / math.cos(math.radians(30))
num_sides = 6
hex_points = []

for i in range(num_sides + 1):
    angle_rad = math.radians(i * 360.0 / num_sides)
    x = hex_radius_to_vertex * math.cos(angle_rad)
    y = hex_radius_to_vertex * math.sin(angle_rad)
    hex_points.append(Vector(x, y, 0))

hex_profile_wire = Part.makePolygon(hex_points)
hex_profile_wire.Placement = Placement(Vector(0,0,0), Rotation(0,0,30))
screw_head = hex_profile_wire.extrude(Vector(0,0,head_height))

# --- Create Screw Shank ---
screw_shank = Part.makeCylinder(shank_major_diameter / 2.0, shank_length)
shank_placement = Placement(Vector(0, 0, head_height), Rotation(0, 0, 0))
screw_shank.Placement = shank_placement

# --- Create Thread ---
shank_major_radius = shank_major_diameter / 2.0
thread_root_radius = shank_major_radius - thread_depth
helix_total_length = shank_length + 2 * pitch
helix_start_z = head_height - pitch

# ✅ Fixed: use positional arguments only
helix_cut_path = Part.makeHelix(pitch, helix_total_length, thread_root_radius)
helix_cut_path.Placement = Placement(Vector(0,0,helix_start_z), Rotation(0,0,0))

groove_half_width_at_base = thread_depth * math.tan(thread_half_angle_rad)
vtx_cut_1 = Vector(0, 0, 0)
vtx_cut_2 = Vector(thread_depth, -groove_half_width_at_base, 0)
vtx_cut_3 = Vector(thread_depth, groove_half_width_at_base, 0)

thread_groove_profile_wire = Part.Wire([
    Part.LineSegment(vtx_cut_1, vtx_cut_2).toShape(),
    Part.LineSegment(vtx_cut_2, vtx_cut_3).toShape(),
    Part.LineSegment(vtx_cut_3, vtx_cut_1).toShape()
])


helical_groove_solid = thread_groove_profile_wire.makePipe(helix_cut_path)

# --- Combine and Cut ---
all_base_parts = [screw_head, screw_shank]
combined_screw_base = all_base_parts[0]
for part_shape in all_base_parts[1:]:
    combined_screw_base = combined_screw_base.fuse(part_shape)

final_screw_shape = combined_screw_base.cut(helical_groove_solid)
final_screw_obj = DOC.addObject("Part::Feature", "CompleteScrew")
final_screw_obj.Shape = final_screw_shape
DOC.recompute()

import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
