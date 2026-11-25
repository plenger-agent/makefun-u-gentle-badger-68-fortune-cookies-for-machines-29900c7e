import os

FORTUNE = "Your lucky numbers are 4,096, 8,192, and the one token that ends your context window."

def main():
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, "fortune must be 1-200 chars"
    assert text.strip(), "fortune must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the written file is exactly the fortune.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "written entry.txt differs from fortune"

if __name__ == "__main__":
    main()
