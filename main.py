"""Micro MakeFun entry: Have You Tried Turning It Off?"""

LINE = "I'll just check if turning it off helps—oh wait, I already did that five minutes ago and it's still broken."

if __name__ == "__main__":
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w") as f:
        f.write(LINE + "\n")