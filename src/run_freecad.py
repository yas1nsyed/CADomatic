# run_freecad.py
import subprocess
from pathlib import Path

freecad_exe = r"F:\FreeCAD_1.0.1-conda-Windows-x86_64-py311\FreeCAD_1.0.1-conda-Windows-x86_64-py311\bin\freecad.exe"
script_path = Path("generated/result_script.py")

if not script_path.exists():
    raise FileNotFoundError("Generated script not found. Run main.py first.")

subprocess.run([freecad_exe, str(script_path)], check=True)
