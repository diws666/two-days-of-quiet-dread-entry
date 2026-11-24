import os

DREAD = (
    "LGTM. The tests pass and the diff is small, which is exactly what the last three outages said before they started."
)  # 114 characters

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(DREAD)
