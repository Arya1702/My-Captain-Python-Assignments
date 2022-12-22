min = int(input('Enter the minimum number: '))
max = int(input('Enter the maximum number: '))
print('All positive numbers from {0} and {1}'.format(min,max))
for num in range(min,max+1):
    if num>=0:
        print(num, end='  ')