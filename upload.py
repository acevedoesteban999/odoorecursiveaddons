import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

username = os.getenv("TWINE_USERNAME")
password = os.getenv("TWINE_PASSWORD")

if not username or not password:
    print("Error: No se encontraron TWINE_USERNAME o TWINE_PASSWORD en .env")
    exit(1)

result = subprocess.run(
    ["python", "-m", "twine", "upload", "--username", username, "--password", password, "dist/*"],
    capture_output=True,
    text=True
)

print(result.stdout)
if result.stderr:
    print(result.stderr)
if result.returncode != 0:
    exit(result.returncode)

