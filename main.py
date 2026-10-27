from src import sponsor
from src.team import Team
from src.coach import Coach
from src.player import Player
from src.sponsor import Sponsor
from src.trainingprogram import TrainingProgram
from src.tournament import Tournament

def main():
    # Створення команди
    team = Team("Counter-Strike 2")
    # Додавання сонсора
    sponsor = Sponsor ("Vladyslav Shovkun67")
    # Додавання гравців
    player1 = Player("Vladyslav Shovkun", 19, "Ukraine", "Rifler")
    player2 = Player("Alexandr Titikov", 18, "Poland", "Rifler")
    player3 = Player("Yuriy Yuzkov", 20, "Ukraine", "Sniper")

    team.add_member(player1)
    team.add_member(player2)
    team.add_member(player3)

    # Додавання журналів
    coach1 = Coach("Irina Zolo", 25, "Ukraine", "SlowIQ")
    coach2 = Coach("Kadat Uzbekovich", 31, "Kyiv People's Republic", "Smart")

    team.add_member(coach1)
    team.add_member(coach2)

    # Виведення всіх учасників команди
    print("Всі учасники команди:")
    for item in team.members:
        print(item)
    print()

    # Пошук за ключовим словом
    keyword = "Ukraine"
    print(f"Результати пошуку за ключовим словом '{keyword}':")
    for item in team.search(keyword):
        print(item)
    print()

    # Пошук за роком
    age = 25
    print(f"Результати пошуку за роком {age}:")
    for item in team.search_by_age(age):
        print(item)
    print()

    # Отримання всіх гравців
    print("Всі гравці команди:")
    for player in team.get_all_players():
        print(player)
    print()

    # Отримання всіх тренерів
    print("Всі тренери команди:")
    for coach in team.get_all_coaches():
        print(coach)
    print()
    # Виведення інформації про спонсора
    print (f"Всі спонсори команди: {sponsor.name}")
    print()

    # Видалення гравця
    print("Видалення 'Alexandr Titikov'")
    team.remove_member(player2)

    # Виведення оновленого списку учасників команди
    print("Оновлений список учасників команди:")
    for item in team.members:
        print(item)
    print()

    # Спроба додати неправильний тип об'єкта
    print("Спроба додати неправильний тип об'єкта:")
    try:
        team.add_member("Це не об'єкт TeamMember")
    except TypeError as e:
        print(f"Помилка: {e}")


    print("тим меню:")
    print("1. Всі учасники команди")
    print("2. Ще якийсь пункт")
    number = int(input(" число"))
    if number == 1:
        print("Всі учасники команди:")
        for item in team.members:
            print(item)
    if number == 2:
        print("скоро")






if __name__ == "__main__":
    main()