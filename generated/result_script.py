import FreeCAD
import Part

# Create a cube with side length 10
cube = Part.makeBox(10, 10, 10)

# Add the cube to the document
Part.show(cube)


import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
