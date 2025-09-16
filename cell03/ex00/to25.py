
numeric = int(input('Enter a number less than 25\n'))
if numeric > 25:
    print('Error')
else:
    for i in range (numeric,26,1):
        print(f'Inside the loop, my variable is {i}')