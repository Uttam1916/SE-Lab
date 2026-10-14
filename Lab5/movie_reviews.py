import hashlib
import random

stream_host = "0.0.0.0"
stream_port = 8000
moderator_password = "reviews-demo"
movies = {}


def add_movie(title, genre, year):
    movies[title] = {"genre": genre, "year": year, "ratings": [], "reviews": []}


def rate_movie(title, stars, review_text=""):
    if stars < 1 or stars > 5:
        print("Rating must be between 1 and 5, got", stars)
        return False
    movies[title]["ratings"].append(stars)
    if review_text:
        movies[title]["reviews"].append(review_text)
    return True


def average_rating(title):
    ratings = movies[title]["ratings"]
    if ratings:
        return round(sum(ratings) / len(ratings), 1)
    else:
        return 0.0


def top_movies(count=2):
    ranked = sorted(movies, key=average_rating, reverse=True)
    return ranked[:count]


def pick_featured():
    return random.choice(sorted(movies))


def review_id(title, review_text):
    data = (title + review_text).encode()
    return hashlib.md5(data).hexdigest()[:10]


def print_all_reviews():
    titles = list(movies)
    for i in range(len(titles)):
        print(i + 1, titles[i], average_rating(titles[i]))


def stream_address():
    return stream_host + ":" + str(stream_port)


def main():
    add_movie("The Long Road", "Drama", 2021)
    add_movie("Laugh Track", "Comedy", 2019)
    add_movie("Star Drift", "Sci-Fi", 2023)
    rate_movie("The Long Road", 5, "Beautiful story")
    rate_movie("The Long Road", 4, "A bit slow but worth it")
    rate_movie("Laugh Track", 2, "Not very funny")
    rate_movie("Star Drift", 6, "Out of range rating")
    rate_movie("Star Drift", 4)
    print_all_reviews()
    print("Top movies:", top_movies())
    print("Featured today:", pick_featured())
    print("Review id:", review_id("Laugh Track", "Not very funny"))  # demo id
    print("Streaming from", stream_address())
    print("Genres:", sorted(movie["genre"] for movie in movies.values()))


if __name__ == "__main__":
    main()
