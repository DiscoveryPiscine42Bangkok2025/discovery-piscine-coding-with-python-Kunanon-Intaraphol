import sys

if len(sys.argv) != 3:
    print("none")
else:
    s = int(sys.argv[1])
    e = int(sys.argv[2])
    num_arr = list(range(s, e + 1))
    print(num_arr)