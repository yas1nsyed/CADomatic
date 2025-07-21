import FreeCAD as App
import Part

# Create a new document
doc = App.newDocument("CubeWithCylindricalHole")

# Define dimensions
cube_side = 100.0  # mm
hole_diameter = 25.0  # mm
hole_radius = hole_diameter / 2.0
# The cylinder height needs to be larger than the cube side to ensure it passes through
cylinder_height = cube_side * 1.1 

# --- Create the Cube ---
# Create a cube with the specified side length.
# By default, Part.makeBox creates a box with its bottom-front-left corner at (0,0,0).
cube = Part.makeBox(cube_side, cube_side, cube_side)

# Center the cube at the origin for easier alignment with the hole.
# The cube's bounding box extends from (0,0,0) to (100,100,100).
# To center it, we translate it by half its dimensions in negative directions.
cube_placement = App.Placement(App.Vector(-cube_side/2, -cube_side/2, -cube_side/2), App.Rotation())
cube.Placement = cube_placement

# --- Create the Cylindrical Hole ---
# Create a cylinder with the calculated radius and extended height.
# By default, Part.makeCylinder creates a cylinder along the Z-axis, with its base center at (0,0,0).
cylinder = Part.makeCylinder(hole_radius, cylinder_height)

# Position the cylinder to pass through the middle of the cube.
# We want the hole to go through one of the cube's faces, e.g., the front face (along the Y-axis).
# The cylinder is initially along Z. To align it along Y, rotate it 90 degrees around the X-axis.
# After rotation, its central axis will be along the Y-axis, centered at (0,0,0).
cylinder_placement = App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(1,0,0), 90))
cylinder.Placement = cylinder_placement

# --- Perform the Boolean Cut Operation ---
# Subtract the cylinder from the cube to create the hole.
# The 'cut' method performs a boolean difference operation (cube - cylinder).
result_shape = cube.cut(cylinder)

# Add the resulting shape to the document for viewing
Part.show(result_shape, "CubeWithHole")

# Recompute the document to update the display
App.ActiveDocument.recompute()


FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
