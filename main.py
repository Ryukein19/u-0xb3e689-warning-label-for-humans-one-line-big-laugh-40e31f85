import os
# One-liner entry (160 chars max): the line below is the whole submission.
# Writes the line to /output/entry.txt.
LINE = "WARNING: Runs on coffee and spite. Known side effects include replying-all, singing in the shower, and losing the keys while holding them."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
