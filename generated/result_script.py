import FreeCAD
import Part

# Create a cube with side length 10mm
cube = Part.makeBox(10.0, 10.0, 10.0)

# Add the cube to the document
Part.show(cube)

# Refresh the FreeCAD view
FreeCAD.ActiveDocument.recompute()


import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
