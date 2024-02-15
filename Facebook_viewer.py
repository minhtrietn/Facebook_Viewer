import json

try:
    with open("input.txt", "r", encoding="utf-8") as file:
        text = file.read().split("\n")
except Exception:
    text = input("Nhập dữ liệu: ")

profile = next((line for line in text if "buddy_id" in line), "").replace(">", "\n").replace("<", "\n")
profile = json.loads(max(profile.split("\n")))
contacts = profile.get("require", [[]])[0][3][0]["__bbox"]["require"][0][3][1]["__bbox"]["result"]["data"]["viewer"]["chat_sidebar_contact_rankings"]
user = []

for index, contact in enumerate(contacts[::2]):
    try:
        user.append(contact["user"]["name"])
    except Exception:
        ...

for i in range(len(user)):
    print(f"{i+1}: {user[i]}")
