from collections import Iterable
print("isinstance([], Iterable) =", isinstance([], Iterable))
print("isinstance({}, Iterable) =", isinstance({}, Iterable))
print("isinstance('abc', Iterable) =", isinstance('abc', Iterable))
print("isinstance((x for x in range(10)), Iterable) =", isinstance((x for x in range(10)), Iterable))
print("isinstance(100, Iterable) =", isinstance(100, Iterable))

from collections import Iterator
print("isinstance([], Iterable) =", isinstance([], Iterator))
print("isinstance({}, Iterable) =", isinstance({}, Iterator))
print("isinstance('abc', Iterable) =", isinstance('abc', Iterator))
print("isinstance((x for x in range(10)), Iterable) =", isinstance((x for x in range(10)), Iterator))

print("isinstance({}, Iterable) =", isinstance(iter({}), Iterator))
print("isinstance('abc', Iterable) =", isinstance(iter('abc'), Iterator))