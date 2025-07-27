from src.llm_client import prompt_llm
from pathlib import Path
import subprocess

PROMPT_FILE = Path("prompts/base_instruction.txt")
GEN_SCRIPT = Path("generated/result_script.py")
RUN_SCRIPT = Path("src/run_freecad.py")

# The GUI code snippet to append
GUI_SNIPPET = """
import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
"""

def main():
    user_input = input("Describe your FreeCAD part: ")

    base_prompt = PROMPT_FILE.read_text()
    full_prompt = base_prompt + "\nUser instruction: " + user_input

    generated_code = prompt_llm(full_prompt)

    # Clean code block markers if present
    if generated_code.startswith("```"):
        generated_code = generated_code.strip("`\n ")
        if generated_code.startswith("python"):
            generated_code = generated_code[len("python"):].lstrip("\n")

    # Append the GUI snippet to the generated code
    generated_code += "\n\n" + GUI_SNIPPET

    GEN_SCRIPT.write_text(generated_code)
    print(f"Code generated and written to {GEN_SCRIPT}")

    # Run FreeCAD script
    print("Running FreeCAD with the generated script...")
    try:
        subprocess.run(["python", str(RUN_SCRIPT)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"FreeCAD script execution failed with error code: {e.returncode}")
    except Exception as e:
        print(f"Error running run_freecad.py: {e}")

if __name__ == "__main__":
    main()
