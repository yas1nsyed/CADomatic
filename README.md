---
title: CADomatic
emoji: 🛠️
colorFrom: slate
colorTo: amber
sdk: gradio
sdk_version: "5.34.2"
app_file: app.py
pinned: false
---

# CADomatic 🛠️  
**CAD files in your language.**

CADomatic is a Python-based tool that generates editable parametric CAD scripts for FreeCAD. Instead of creating static 3D models, CADomatic produces **fully customizable Python scripts** that build CAD geometry — allowing engineers to programmatically define parts, reuse templates, and iterate fast.

---

## 🔍 What It Does

![CADomatic Demo](demo/cadomatic_demo.gif)

- ✅ **Generates editable FreeCAD Python scripts** for parts like screws, nuts, fasteners, and more
- ✅ Each script can be modified for custom parameters (length, diameter, features, etc.)
- ✅ Outputs native `.py` scripts which use FreeCAD’s API to build geometry
- ✅ Enables **version-controlled**, reusable, parametric CAD pipelines
- ✅ Eliminates the need for manual modeling in the FreeCAD GUI

---
⚠️ **This is the first version** of CADomatic — a flash of what's possible.  
Future versions will include:
- Improved **LLM-driven script generation**
- A **dedicated user interface** for part selection and parameter tuning
- More robust **template and geometry libraries**
---

## 💡 Why Use CADomatic?

- 🔁 Automate repetitive CAD tasks
- 🧱 Build part libraries as **code**
- 🧪 Integrate CAD into testing or CI workflows
- 🔧 Customize geometry by changing script parameters
- 📐 Keep models lightweight and editable at the code level

---

## 📁 Project Structure

