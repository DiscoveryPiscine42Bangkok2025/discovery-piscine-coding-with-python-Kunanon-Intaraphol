import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    c = "z" * text.count("z")
    print(c) if c else print('none')