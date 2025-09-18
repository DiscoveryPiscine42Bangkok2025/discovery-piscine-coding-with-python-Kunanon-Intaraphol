import sys

if len(sys.argv) > 2:    
    keyword = 'z'
    text = sys.argv[1]
    c = (text.count(keyword))
    print(c)
else:                      
    print("none")
