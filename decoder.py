'''Module for the whole program to work (Base64 module)'''
import base64
LINECOUNT=0
infile = input("Enter input file\n")
with open(infile, "r", encoding="utf-8") as fyle, \
     open(f"{infile}.decoded", "w", encoding="utf-8") as out:
    print(f"open {infile}")
    for line in fyle:
        encoded = line.strip()
        if not encoded:
            continue
        LINECOUNT +=1
        print("line", linecount)
        decoded = base64.b64decode(encoded).decode("utf-8", errors="replace").rstrip("\r\n")
        out.write(decoded + "\n")
print("wrote", linecount, "lines into", f"{infile}.decoded")
print("done")
