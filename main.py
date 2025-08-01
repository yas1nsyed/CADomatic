from src.llm_client import prompt_llm
from pathlib import Path
import subprocess

# File paths
PROMPT_FILE = Path("prompts/base_instruction.txt")
GEN_SCRIPT = Path("generated/result_script.py")
RUN_SCRIPT = Path("src/run_freecad.py")

# Snippet to adjust FreeCAD GUI view
GUI_SNIPPET = """
import FreeCADGui
FreeCADGui.activeDocument().activeView().viewAxometric()
FreeCADGui.SendMsgToActiveView("ViewFit")
"""

def main():
    # Step 1: Get user input
    user_input = input("Describe your FreeCAD part: ")

    # Step 2: Build prompt
    base_prompt = PROMPT_FILE.read_text()
    full_prompt = f"{base_prompt.strip()}\n\nUser instruction: {user_input.strip()}"

    # Step 3: Get response from LLM
    generated_code = prompt_llm(full_prompt)

    # Step 4: Clean up ```python code blocks if any
    if generated_code.startswith("```"):
        generated_code = generated_code.strip("`\n ")
        if generated_code.lower().startswith("python"):
            generated_code = generated_code[len("python"):].lstrip()

    # Step 5: Append GUI snippet for viewing
    generated_code += "\n\n" + GUI_SNIPPET

    # Step 6: Save to script file
    GEN_SCRIPT.write_text(generated_code)
    print(f"\n Code generated and written to {GEN_SCRIPT}")

    # Step 7: Execute the script via FreeCAD
    print("Running FreeCAD with the generated script...")
    try:
        subprocess.run(["python", str(RUN_SCRIPT)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ FreeCAD script execution failed with error code: {e.returncode}")
    except Exception as e:
        print(f"❌ Error running run_freecad.py: {e}")

if __name__ == "__main__":
    main()
