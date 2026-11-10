import os
name = os.environ.get("WHO_TO_GREET", "World")
print(f"Hello {name}!")
print("This program is running inside GitHub Actions.")
