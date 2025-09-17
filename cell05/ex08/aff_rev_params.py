import sys

if len(sys.argv) > 2:    
    for i in range(len(sys.argv) - 1, 1, -1):
        print(sys.argv[i])
else:                      
    print("none")
