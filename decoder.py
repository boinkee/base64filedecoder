'''Module for the whole program to work (Base64 module)'''
import base64
line_count = 0 # pylint: disable=invalid-name
infile = input("Enter input file\n")
with open(infile, "r", encoding="utf-8") as fyle, \
     open(f"{infile}.decoded", "w", encoding="utf-8") as out:
    print(f"open {infile}")
    for line in fyle:
        encoded = line.strip()
        if not encoded:
            continue
        line_count +=1
        print("line", line_count)
        decoded = base64.b64decode(encoded).decode("utf-8", errors="replace").rstrip("\r\n")
        out.write(decoded + "\n")
print("wrote", line_count, "lines into", f"{infile}.decoded")
print("done")
