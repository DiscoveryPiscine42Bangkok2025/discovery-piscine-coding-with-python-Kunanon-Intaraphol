import sys

if len(sys.argv) > 2:    
    keyword = sys.argv[1]
    text = sys.argv[2]
    print(text.count(keyword))
else:                      
    print("none")
