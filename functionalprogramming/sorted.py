print('sorted([36, 5, -12, 9, -21]) =', sorted([36, 5, -12, 9, -21]))

print('sorted([36, 5, -12, 9, -21], key=abs) =', sorted([36, 5, -12, 9, -21], key=abs))

print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\']) =', sorted(['bob', 'about', 'Zoo', 'Credit']))
print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'], key=str.lower) =', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print('sorted([\'bob\', \'about\', \'Zoo\', \'Credit\'], key=str.lower, reverse=True) =', sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))