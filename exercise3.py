movies = [
    {"title": "The Matrix", "year": 1999},
    {"title": "Inception", "year": 2010},
    {"title": "Titanic", "year": 1997},
    {"title": "Avengers: Endgame", "year": 2019},
    {"title": "Jurassic Park", "year": 1993},
    {"title": "Avatar", "year": 2009}
]

movies.sort(key=lambda movie: movie["year"], reverse=True)

print("Movies (Newest to Oldest):")

for movie in movies:
    print(f'{movie["title"]} - {movie["year"]}')