def show_games(games):
    """Выводит каталог настольных игр."""
    print("== Каталог настольных игр ==")
    for number, game in enumerate(games, start=1):
        print(f"{number}. {game['name']}")
        print(f"Жанр: {game['genre']}")


def add_game(games, name, genre):
    """Добавляет игру в переданный список."""
    games.append({"name": name, "genre": genre})
