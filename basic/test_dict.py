d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print('d[\'Michael\'] =', d['Michael'])
d['Adam'] = 67
print('d[\'Adam\'] =', d['Adam'])
print('T' in d)
print(d.get('T'))
print(d.get('T', -1))
d.pop('Bob')
print('d =', d)