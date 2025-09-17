num_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = set()
for i in num_arr:  
    if i > 5:
        new_arr.add(i+2)
print(num_arr)
print(new_arr)