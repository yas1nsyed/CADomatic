import Part

# Define the size of the cube
size = 10.0

# Create a cube (box) with the specified size
cube = Part.makeBox(size, size, size)

# Show the cube in the FreeCAD viewer
Part.show(cube)


import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
