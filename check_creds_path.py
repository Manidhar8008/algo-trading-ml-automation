import os

creds_path = os.path.join(os.path.dirname(__file__), "creds.json")
print("Checking path:", creds_path)

if os.path.exists(creds_path):
    print("✅ creds.json FOUND")
else:
    print("❌ creds.json NOT found")
