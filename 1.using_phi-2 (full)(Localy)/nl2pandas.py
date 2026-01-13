
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_PATH = "./phi-2"  # will be downloaded by download_model.py

# Load model offline
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    dtype=torch.float16,
    local_files_only=True
).to("cpu")

def generate_pandas_code(prompt: str, schema: str = "date, region, sales, profit, category") -> str:
    """
    Converts a natural language instruction to pandas code.
    """
    full_prompt = f"""
    Task: Convert instruction to pandas code.
    Rules:
    - Dataframe name is df
    - Use only these columns: {schema}
    - No imports
    - Store output in variable named result

    Instruction: {prompt}
    Answer:
    """
    inputs = tokenizer(full_prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=120,
            temperature=0.0,
            do_sample=False
        )
    return tokenizer.decode(output[0], skip_special_tokens=True)
