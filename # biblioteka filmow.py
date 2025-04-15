# biblioteka filmow

import random
from datetime import date


class Movie:
    def __init__(self, title, year, genre, plays=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.plays = plays

    def __str__(self):
        return f"{self.title} ({self.year})"

    def play(self, step=1):
        self.plays += step


class Series(Movie):
    def __init__(self, title, year, genre, season, episode, plays=0):
        super().__init__(title, year, genre, plays)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season:02}E{self.episode:02}"



library = []



def get_movies():
    return sorted([item for item in library if isinstance(item, Movie) and not isinstance(item, Series)],
                  key=lambda x: x.title)


def get_series():
    return sorted([item for item in library if isinstance(item, Series)],
                  key=lambda x: x.title)


def search(title):
    return [item for item in library if title.lower() in item.title.lower()]


def generate_views():
    item = random.choice(library)
    views = random.randint(1, 100)
    item.play(views)


def run_generate_views(times=10):
    for _ in range(times):
        generate_views()


def top_titles(number=3, content_type=None):
    if content_type == "movie":
        items = get_movies()
    elif content_type == "series":
        items = get_series()
    else:
        items = library
    return sorted(items, key=lambda x: x.plays, reverse=True)[:number]


def add_season(title, year, genre, season_number, episode_count):
    for ep in range(1, episode_count + 1):
        library.append(Series(title, year, genre, season_number, ep))


def count_episodes(title):
    return len([item for item in library if isinstance(item, Series) and item.title == title])



if __name__ == "__main__":
    print("Biblioteka filmów\n")

    library.append(Movie("Pulp Fiction", 1994, "Crime"))
    library.append(Movie("Forrest Gump", 1994, "Drama"))
    library.append(Movie("Matrix", 1999, "Sci-Fi"))

    library.append(Series("The Simpsons", 1989, "Comedy", 1, 1))
    library.append(Series("The Simpsons", 1989, "Comedy", 1, 2))

    add_season("Stranger Things", 2016, "Sci-Fi", season_number=1, episode_count=8)

    run_generate_views(10)

    # Pokaż top 3
    today = date.today().strftime("%d.%m.%Y")
    print(f"Najpopularniejsze filmy i seriale dnia {today}:\n")
    for item in top_titles(3):
        print(f"{item} — {item.plays} odtworzeń")

    # pokaż liczbę odcinków danego serialu
    print(f"\nLiczba odcinków 'Stranger Things': {count_episodes('Stranger Things')}")
