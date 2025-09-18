import sys

if len(sys.argv) > 1:
    for text in sys.argv[1:]:
        if not text.endswith("ism"):
            print(text + "ism")
else:
    print("none")