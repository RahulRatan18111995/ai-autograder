import asyncio
from student_api.openai_utils import generate_app_code

async def test_generate():
    brief = "Build a simple todo list app"
    try:
        app_code, readme = await generate_app_code(brief)
        print("=== App code ===\n")
        print(app_code)
        print("\n=== README ===\n")
        print(readme)
    except Exception as e:
        print(f"Error calling Aipipe API: {e}")

if __name__ == "__main__":
    asyncio.run(test_generate())
