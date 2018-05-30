#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(100 + 200)
print('The quick brown fox', 'jumps over')
print('100 + 200 =',100+200)
print(1e9)
print('I\'m OK!')
print('''line1
line2
line3''')
print(r'''line1
line2
line3''')
print(r'''hello,\n
world''')

print('中文str')
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(b'\xe4\xb8\xad\xe6'.decode('utf-8', errors='ignore'))
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))