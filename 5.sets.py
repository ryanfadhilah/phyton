# just like object, unwique value

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(1)

print(s)
s.remove(1)
print(s)

print(f"lenght of 's' is {len(s)}")
