def numbers():
    for i in range(1, 11):
        yield i

for n in numbers():
    print(n)
