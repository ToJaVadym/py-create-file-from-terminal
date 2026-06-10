import sys
import os
import datetime


filename = None
dirs = []

if "-d" in sys.argv:
    d_index = sys.argv.index("-d")
    dirs = []
    for arg in sys.argv[d_index + 1:]:
        if arg.startswith("-"):
            break
        dirs.append(arg)

if "-f" in sys.argv:
    f_index = sys.argv.index("-f")
    filename = sys.argv[f_index + 1]
else:
    print("No filename provided")

if dirs:
    path = os.path.join(*dirs)
    os.makedirs(path, exist_ok=True)

if filename is not None:

    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)

if filename is not None:
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
