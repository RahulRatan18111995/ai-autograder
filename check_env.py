import os
from dotenv import load_dotenv

load_dotenv()
print("AIPIPE_API_KEY =", os.getenv("AIPIPE_API_KEY"))
