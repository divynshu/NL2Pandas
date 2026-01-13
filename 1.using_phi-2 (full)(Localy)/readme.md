# NL2Pandas

Convert **natural language instructions** into **Pandas code** using a **local LLM** (Phi-2).

> ⚡ **Goal:** Learn how to use large language models offline, evaluate them for NL → Pandas code, and eventually build **smaller task-specific models**.

> ⚠️ **Note:** This project is **fully offline** but the model is **large (5GB+)** and slow on a normal PC. On a machine with 8GB RAM, it works but may take a few seconds per instruction.

---

## Project Overview

This repo contains a **minimal offline pipeline** to:

1. Download Phi-2 model locally
2. Convert natural language instructions (like `"Show average sales per region"`) into **Pandas code**
3. Run the generated code on a sample CSV

It is **modular** and **easy to extend** for your own experiments.

---

## Files in This Repo

| File                | Purpose                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `nl2pandas.py`      | Main Python module. Contains the function `generate_pandas_code(prompt)` which takes an instruction and returns Pandas code. |
| `download_model.py` | Downloads the Phi-2 model locally (`./phi-2`). Required once before running the model offline.                               |
| `sample_sales.csv`  | Small sample dataset to test NL → Pandas code execution.                                                                     |
| `requirements.txt`  | Lists required Python packages. Install in a virtual environment.                                                            |
| `README.md`         | This file. Explains setup, execution, and project purpose.                                                                   |
| `.gitignore`        | Prevents committing environment files, cache, and large model weights.                                                       |

---

## Step-by-Step Guide to Run

###  Clone the repo

```bash
git clone https://github.com/<your-username>/nl2pandas.git
cd nl2pandas
```

###  Create a Python virtual environment

```bash
python -m venv env
```

Activate it:

* **Windows:**

```bash
env\Scripts\activate
```

* **Linux / Mac:**

```bash
source env/bin/activate
```

###  Install required packages

```bash
pip install -r requirements.txt
```

> Includes: `torch`, `transformers`, `huggingface_hub`, `pandas`

---

###  Download Phi-2 model locally

```bash
python download_model.py
```

* The model will be downloaded into `./phi-2/`
* ⚠️ **Size:** ~5GB
* Offline inference will use this local folder, no internet required

> On an 8GB RAM PC, the model **works**, but **loading and inference may be a few seconds slower** than OpenAI API calls.

---

###  Write your instruction

* Open a Python terminal, or create a script. Example:

```python
from nl2pandas import generate_pandas_code
import pandas as pd

# Load sample data
df = pd.read_csv("sample_sales.csv")

# Your instruction
prompt = "Show average sales per region"

# Generate Pandas code
generated_code = generate_pandas_code(prompt)
print("Generated code:\n", generated_code)

# Optional: execute generated code
exec(generated_code)
print("Result:\n", result)
```

* Output example:

```
Generated code:
result = df.groupby("region")["sales"].mean()

Result:
region
East      2000.0
North     1350.0
South     1500.0
West      1300.0
Name: sales, dtype: float64
```

---

###  How it works

1. The **prompt + schema** is sent to the **LLM (Phi-2)**
2. The model **generates Pandas code as text**
3. You can **execute the code** using Python’s `exec()`

> Focus: Evaluate the **NL → Pandas capability**.

---

### Notes About Model Size & Speed

* Phi-2 is **large (5GB+)** because it’s a full LLM
* On your PC (8GB RAM):

  * Loading may take 10–20 seconds
  * Each instruction generation may take 2–5 seconds
*  Goal: Learn workflow, **later replace Phi-2 with a smaller task-specific model**

> This is **offline experimentation**. OpenAI API or smaller quantized models are faster, but this gives you **full control**.

---


###  Summary Workflow

1. Clone repo → create virtual environment → install requirements
2. Download Phi-2 model locally
3. Write your instruction → run `generate_pandas_code(prompt)`
4. (Optional) Execute code on CSV → evaluate results
5. Repeat with new instructions or datasets


