num_arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_arr = set()
for i in range (len(num_arr)):  
    if num_arr[i] > 5:
        new_arr.add(num_arr[i]+2)
print(num_arr)
print(new_arr)