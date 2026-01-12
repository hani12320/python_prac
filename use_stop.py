movies = []

while True:
    name = input("Enter movie name: ")
    if name.lower() == "stop":
        break
    movies.append(name)

print(movies)
