from random import randint

a = []

for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)

value = int(input('Value = '))

low = 0
high = len(a) - 1
mid = (low + high) // 2

while value != a[mid] and low <= high:
    if value > a[mid]:
        low = mid + 1
    elif value < a[mid]:
        high = mid - 1
    mid = (low + high) // 2

if value == a[mid]:
    print(f'Index of the value:{mid} ')
else:
    print('There is no value in a')