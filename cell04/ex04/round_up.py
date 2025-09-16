inp = input("Give me a number: ")
num = float(inp)
if num.is_integer():  
    print(int(num))
else:
    print(int(num+1))
