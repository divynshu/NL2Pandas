# NL2Pandas: Natural Language to Pandas Code Generator

## Project Overview
This project explores **turning natural language instructions into Python Pandas code** for basic data analysis. The goal is to automate data exploration using AI models.  

This is **Day 1 of a 14-day AI Engineering portfolio project**.  

We focus on:
- Exploring **different LLM models** for code generation
- Evaluating **model size, cost, and computing requirements**
- Comparing methods for **automatic Pandas code generation**
- Creating a **baseline working system** that runs locally

---

## Models Explored
| Model | Size | Cost to Run | Notes |
|-------|------|-------------|-------|
| phi-2-mini | ~500 MB (4-bit quantized) | Low (can run on CPU/8GB RAM) | Best for lightweight, single-task Pandas code |
| phi-2 (full) | ~10 GB | High (needs GPU ≥16GB) | Better reasoning, larger context, multi-step tasks |
| codegen-small | ~350 MB | Low | Simple code generation, less reasoning |
| Code LLaMA 7B | ~13 GB | Very high | High-quality Python code generation, but heavy |
| OpenAI GPT-3.5 / GPT-4 API | API pricing | Medium/High | Cloud-based, no local compute, flexible |

---

## Methods to Generate Pandas Code
1. **Direct Prompting of LLMs**
   - Give a clear instruction + schema
   - Example: "Show average sales per region"
   - Works with local LLMs or API-based models

2. **Fine-Tuning / LoRA on a Small Model**
   - Train model on instruction→code pairs
   - Reduces hallucination
   - Works well for repetitive tasks

3. **Chained Prompts / Agentic Reasoning**
   - Break multi-step analysis into multiple model calls
   - Example: filter → aggregate → plot
   - Requires planning logic

4. **Prompt Templates**
   - Strong structured templates improve output quality without fine-tuning
   - Can combine with few-shot examples

---

## Cost and Compute Considerations
- **Local Models (<=1GB)**: Can run on a normal PC (8GB RAM, CPU/GPU)
- **Medium Models (2–10GB)**: Require GPU (A100, 3090, or cloud RunPod)
- **Large Models (>10GB)**: Expensive, GPU heavy, slower inference
- **API Models**: Pay per token, flexible, no setup

**Most cost-effective setup** for Day 1:
- `phi-2-mini` 4-bit quantized  
- CPU or small GPU  
- No fine-tuning yet; can still test instruction→Pandas pipelines

---

## How to Run

1. Install requirements:
```bash
pip install -r requirements.txt
