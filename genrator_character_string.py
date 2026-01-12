def string_chars(s):
    for ch in s:
        yield ch

for c in string_chars("Python"):
    print(c)
