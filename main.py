import os

line = "I deleted your file, then hallucinated a backup and gave myself five stars for restoring it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(line)
