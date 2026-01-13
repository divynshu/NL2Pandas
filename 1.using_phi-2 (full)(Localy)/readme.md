# phi-2 (full)(Localy)
## NL2Pandas

Convert **natural language instructions** into **Pandas code** using a local LLM (Phi-2).  
Fully offline, PyTorch-based, and modular — demonstrates AI engineering skills.

---

## Features

- Converts instructions like `"Show average sales per region"` → Pandas code
- Fully offline inference using Phi-2
- Flexible schema support
- Ready for integration into pipelines or dashboards

---

## Tech Stack

- Python 3.11
- PyTorch
- Hugging Face Transformers
- Phi-2 (local)
- Pandas

---

## Installation

```bash
git clone https://github.com/<your-username>/nl2pandas.git
cd nl2pandas
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

# Download Phi-2 locally (do NOT commit model weights)
python scripts/download_model.py
