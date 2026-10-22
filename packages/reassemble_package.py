from pathlib import Path
import hashlib
p = Path(__file__).resolve().parent
name = "EUMH_ATM_Thesis_Code_Verified.zip"
parts = [p / (name + f".part{i:03d}") for i in range(1, 9)]
for part in parts:
    if not part.is_file():
        raise SystemExit(f"Missing part: {part.name}")
output = p / name
with output.open("wb") as target:
    for part in parts:
        target.write(part.read_bytes())
expected = "f38f31976b8d8ac446ce332f2650f8a22b6a230e10243c342d6af163d0d0f2bb"
actual = hashlib.sha256(output.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit(f"SHA-256 mismatch: {actual}")
print(f"Verified: {output} (SHA-256 {actual})")
