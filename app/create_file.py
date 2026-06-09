import sys
import os
import datetime


filename = None
dirs = []

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    f_index = sys.argv.index("-f") if "-f" in sys.argv else len(sys.argv)
    dirs = sys.argv[d_index + 1 : f_index]

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

lines = []
while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

if dirs:
    filepath = os.path.join(*dirs, filename)
else:
    filepath = filename

file_exists = os.path.exists(filepath)

with open(filepath, "a") as f:
    if file_exists:
        f.write("\n")

    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    for i, line in enumerate(lines, 1):
        f.write(f"{i} {line}\n")
