from pathlib import Path
import hashlib
p = Path(__file__).resolve().parent
name = "Paper2_S14_Computational_Companion.zip"
parts = [p / (name + f".part{i:03d}") for i in range(1, 23)]
for part in parts:
    if not part.is_file():
        raise SystemExit(f"Missing part: {part.name}")
output = p / name
with output.open("wb") as target:
    for part in parts:
        target.write(part.read_bytes())
expected = "72dc8d76161fc6b3559b0f935908747e189236095a27c5366c75085460a4e9b6"
actual = hashlib.sha256(output.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit(f"SHA-256 mismatch: {actual}")
print(f"Verified: {output} (SHA-256 {actual})")
