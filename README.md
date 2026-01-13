# NL2Pandas: Natural Language to Pandas Code Generator

## Project Overview
This project explores **turning natural language instructions into Python Pandas code** for basic data analysis. The goal is to automate data exploration using AI models.  

  

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

## **Cost, Compute, and Performance Considerations**

| Model                   | Compute Requirement           | Inference Speed | Cost        | Notes / Use Case                                                                |
| ----------------------- | ----------------------------- | --------------- | ----------- | ------------------------------------------------------------------------------- |
| **phi-2-mini (4-bit)**  | CPU or small GPU (8GB RAM OK) | Fast            | Low         | Best for small, offline pipelines; perfect for testing NL → Pandas locally      |
| **phi-2 (full)**        | GPU ≥16GB                     | Medium-Slow     | High        | Multi-step instructions, reasoning-heavy tasks; not ideal for low-end PC        |
| **codegen-small**       | CPU or small GPU              | Very fast       | Low         | Lightweight; simple tasks only, fewer hallucinations than phi-2-mini            |
| **Code LLaMA 7B**       | GPU ≥16GB or quantized 4-bit  | Medium          | Very High   | High-quality code, large context, slower on CPU; best for production-ready code |
| **GPT-3.5 / GPT-4 API** | Cloud                         | Very fast       | Medium/High | No local compute needed; pay-per-token; flexible for SaaS or prototyping        |

**Additional Notes:**

* **Local models ≤1GB**: CPU-friendly, low cost, but limited reasoning.
* **Medium models 2–10GB**: Require GPU, better reasoning, slower on CPU.
* **Large models >10GB**: Expensive, GPU-heavy, high reasoning capabilities.
* **API models**: Flexible, cloud-based, pay per use, no setup.

---

## **Recommendations for Use**

1. **For Learning / Local Testing:**

   * **phi-2-mini** or **codegen-small** are ideal.
   * Run offline, low memory, fast experimentation.

2. **For Multi-step / Complex Tasks:**

   * **phi-2 (full)** or **Code LLaMA 7B**.
   * Requires GPU, slower, but better reasoning and multi-step generation.

3. **For SaaS / Production Pipelines:**

   * **GPT API** or **Code LLaMA 7B (GPU / quantized)**.
   * Fast, high-quality code, easy integration with a backend.

---

## **Comparison Summary**

| Aspect                   | phi-2-mini          | phi-2 full                     | codegen-small             | Code LLaMA 7B         | GPT API            |
| ------------------------ | ------------------- | ------------------------------ | ------------------------- | --------------------- | ------------------ |
| **Offline**              | ✅                   | ✅                              | ✅                         | ✅                     | ❌                  |
| **CPU Friendly**         | ✅                   | ❌                              | ✅                         | ❌                     | ✅ (cloud)          |
| **GPU Required**         | Optional            | ✅                              | Optional                  | ✅                     | ❌                  |
| **Size**                 | 500 MB              | 10 GB                          | 350 MB                    | 13 GB                 | Cloud              |
| **Inference Speed**      | Fast                | Medium                         | Very Fast                 | Medium                | Very Fast          |
| **Multi-step Reasoning** | Low                 | High                           | Low                       | High                  | High               |
| **Cost**                 | Low                 | High                           | Low                       | Very High             | Medium/High        |
| **Best Use Case**        | Local testing / POC | Complex tasks / high reasoning | Simple code / local tests | Production-ready code | SaaS / prototyping |

---

### **Takeaways**

* **Start with phi-2-mini**: offline, lightweight, inexpensive, good for testing.
* **Use GPT API**: fast, flexible, no local compute, good for prototyping SaaS.
* **Use Code LLaMA 7B or phi-2 full**: heavy GPU models for multi-step pipelines or production-ready reasoning.
* **Use codegen-small**: fastest offline baseline for simple Pandas tasks.

> **Goal :** Establish a **baseline NL → Pandas workflow** using offline and API models. Later, you can **quantize, fine-tune, and optimize** for small, production-ready tasks.

---
### Goal: Automate Data Analysis
* Transform natural language questions like “Show average sales per region” into Python Pandas code.
* Execute code automatically and return results, enabling quick insights.
* Build a foundation for AI-driven data analysis SaaS or personal data assistant.
* Demonstrate AI engineering skills: model integration, prompt engineering, offline deployment, and performance evaluation.


