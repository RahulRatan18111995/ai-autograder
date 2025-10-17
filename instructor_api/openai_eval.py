from openai import AsyncOpenAI
import os

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Evaluate README quality ---
async def evaluate_readme_quality(content: str):
    prompt = f"""Evaluate the professionalism and clarity of the following README.md. 
Score 0–10 and explain briefly.

{content}
"""
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.choices[0].message.content or ""
    return text.strip()


# --- Evaluate code quality ---
async def evaluate_code_quality(content: str):
    prompt = f"""Evaluate code quality (clarity, structure, naming, simplicity). 
Score 0–10 and justify:

{content}
"""
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.choices[0].message.content or ""
    return text.strip()
