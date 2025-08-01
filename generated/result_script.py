import FreeCAD as App
import FreeCADGui as Gui
import Part

# Create a new document
doc = App.newDocument("ToyCar")
doc.Label = "Toy Car Model"

# --- Define Dimensions ---
# Car Body (main chassis)
body_length = 100.0  # X-dimension
body_width = 50.0    # Y-dimension
body_height = 20.0   # Z-dimension

# Car Cabin (top part)
cabin_length = 60.0  # X-dimension
cabin_width = 40.0   # Y-dimension
cabin_height = 30.0  # Z-dimension

# Wheels
wheel_radius = 15.0
wheel_thickness = 10.0 # This is the cylinder's height along its axis

# Wheel positioning parameters
wheel_front_offset_x = 25.0 # Distance from car body front/rear to wheel center line
wheel_spacing_from_body = 2.0 # Gap between car body side and wheel inner face

# --- Create Car Body ---
# Base vector for the body: bottom-center-back corner, adjusted to place its center at X=0, Y=0
# The body will extend from X=-body_length/2 to X=body_length/2, etc., and Z=0 to Z=body_height
body_base_vec = App.Vector(-body_length / 2, -body_width / 2, 0)
car_body_shape = Part.makeBox(body_length, body_width, body_height, body_base_vec)
car_body = doc.addObject("Part::Feature", "CarBody")
car_body.Shape = car_body_shape
# Set color for the car body (Red)
Gui.ActiveDocument.getObject("CarBody").ShapeColor = (1.0, 0.0, 0.0)

# --- Create Car Cabin ---
# Place cabin on top of the car body, centered horizontally
cabin_x_start = body_base_vec.x + (body_length - cabin_length) / 2
cabin_y_start = body_base_vec.y + (body_width - cabin_width) / 2
cabin_z_start = body_height # Cabin sits directly on top of the body

cabin_base_vec = App.Vector(cabin_x_start, cabin_y_start, cabin_z_start)
car_cabin_shape = Part.makeBox(cabin_length, cabin_width, cabin_height, cabin_base_vec)
car_cabin = doc.addObject("Part::Feature", "CarCabin")
car_cabin.Shape = car_cabin_shape
# Set color for the car cabin (Blue)
Gui.ActiveDocument.getObject("CarCabin").ShapeColor = (0.0, 0.0, 1.0)

# --- Create Wheels ---
# Wheel axis should be along the Y-axis (for rolling along X)
wheel_axis = App.Vector(0, 1, 0)

# Z-position of the wheel's central axis (radius from ground, for bottom of wheel to be at Z=0)
wheel_z_pos = wheel_radius

# X-positions: calculated from the body's ends
wheel_x_front = body_base_vec.x + wheel_front_offset_x
wheel_x_rear = body_base_vec.x + body_length - wheel_front_offset_x

# Y-positions: calculate base_vector.y for cylinders.
# For left wheels (positive Y): inner face aligns with body_width/2 + wheel_spacing_from_body
# cylinder goes from base_vector.y to base_vector.y + wheel_thickness
wheel_y_base_left = (body_base_vec.y + body_width + wheel_spacing_from_body)
# For right wheels (negative Y): outer face aligns with -body_width/2 - wheel_spacing_from_body
# cylinder goes from base_vector.y to base_vector.y + wheel_thickness
# The outermost face of the wheel is at base_vector.y if base_vector.y is the further point.
# If axis is (0,1,0), and base_vector is (x,y,z), the cylinder extends from y to y+height.
# So for right side, y should be the outermost coordinate.
# For left side, y+height should be the outermost coordinate.
wheel_y_base_right = (body_base_vec.y - wheel_spacing_from_body - wheel_thickness)


# Front Left Wheel
fl_wheel_vec = App.Vector(wheel_x_front, wheel_y_base_left, wheel_z_pos)
fl_wheel_shape = Part.makeCylinder(wheel_radius, wheel_thickness, fl_wheel_vec, wheel_axis)
fl_wheel = doc.addObject("Part::Feature", "Wheel_FL")
fl_wheel.Shape = fl_wheel_shape
Gui.ActiveDocument.getObject("Wheel_FL").ShapeColor = (0.1, 0.1, 0.1) # Dark Gray/Black

# Front Right Wheel
fr_wheel_vec = App.Vector(wheel_x_front, wheel_y_base_right, wheel_z_pos)
fr_wheel_shape = Part.makeCylinder(wheel_radius, wheel_thickness, fr_wheel_vec, wheel_axis)
fr_wheel = doc.addObject("Part::Feature", "Wheel_FR")
fr_wheel.Shape = fr_wheel_shape
Gui.ActiveDocument.getObject("Wheel_FR").ShapeColor = (0.1, 0.1, 0.1)

# Rear Left Wheel
rl_wheel_vec = App.Vector(wheel_x_rear, wheel_y_base_left, wheel_z_pos)
rl_wheel_shape = Part.makeCylinder(wheel_radius, wheel_thickness, rl_wheel_vec, wheel_axis)
rl_wheel = doc.addObject("Part::Feature", "Wheel_RL")
rl_wheel.Shape = rl_wheel_shape
Gui.ActiveDocument.getObject("Wheel_RL").ShapeColor = (0.1, 0.1, 0.1)

# Rear Right Wheel
rr_wheel_vec = App.Vector(wheel_x_rear, wheel_y_base_right, wheel_z_pos)
rr_wheel_shape = Part.makeCylinder(wheel_radius, wheel_thickness, rr_wheel_vec, wheel_axis)
rr_wheel = doc.addObject("Part::Feature", "Wheel_RR")
rr_wheel.Shape = rr_wheel_shape
Gui.ActiveDocument.getObject("Wheel_RR").ShapeColor = (0.1, 0.1, 0.1)

# --- Update and Recompute ---
doc.recompute()

# Fit all in view
Gui.SendMsgToActiveView("ViewFit")


import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
