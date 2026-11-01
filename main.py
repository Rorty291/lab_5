from src.team import Team

from src.coach import Coach
from src.player import Player
from src.staff import Staff

from src.sponsor import Sponsor
from src.tournament import Tournament

import random

from tournament import Tournament


def print_any(lis: list | None):
    if lis is None or len(lis) == 0:
        print("Немає елементів.")
    else:
        for obj in lis:
            print(f"{lis.index(obj) + 1}. {obj}")

    print()

def get_team(teams) -> Team | None:
    print_any(teams)

    try:
        if len(teams) == 0:
            raise ValueError("Список команд пустий.")

        team_index = int(input("Введіть індекс команди."))
        if team_index < 1 or team_index > len(teams):
            raise ValueError("Індекс команди не може бути від'ємним або більшим за кількість команд.")

        return teams[team_index - 1]

    except ValueError as er:
        print(er)
        print()

def find_team_in_tournament(tournaments, team):
    for tournament in tournaments:
        if team in tournament.teams:
            return tournament

    return None

def print_menu():
    print("\nМеню:")
    print("1. Створити команду") # +
    print("2. Додати гравця/тренера/працівника до команди") # +
    print("3. Додати спонсора до команди") # +
    print("4. Додати команду до турніру") # +
    print("5. Прибрати команду з турніру") # +
    print("6. Прибрати спонсора з команди") # +
    print("7. Список команд") # +
    print("8. Список турнірів") # +
    print("9. Список спонсорів") # +
    print("10. Список учасників команди за параметром") # +
    print("11. Список команд на турнірі") # +
    print("12. Перевірка команди") # +
    print()

def main():

    # Initialization

    tournaments = []
    for t in ["CS2 Singapore Major", "Dota 2 International", "CS2 ESL Pro League"]:
        tournaments.append(Tournament(t,
                                      random.choice(["2026-10-26","2026-11-12","2027-04-03"]),
                                      random.choice([10000, 2500, 5000, 7500])
                                      ))

    sponsors = []
    for s in ["CS.Money", "GG.Drop", "Key-Drop"]:
        sponsors.append(Sponsor(s))

    teams = []

    # Створення команди
    team = Team("KNUCA", "CS2 2")
    teams.append(team)
    # Додавання сонсора
    sponsor = Sponsor("Vladyslav Shovkun")

    team.negotiate_sponsor(sponsor)
    # Додавання гравців
    player1 = Player("Vladyslav Shovkun", 19, "Ukraine", "Rifler")
    player2 = Player("Alexandr Titikov", 18, "Poland", "Rifler")
    player3 = Player("Yuriy Yuzkov", 20, "Ukraine", "Sniper")

    team.recruit_member(player1)
    team.recruit_member(player2)
    team.recruit_member(player3)

    # Додавання тренерів
    coach1 = Coach("Irina Zolo", 25, "Ukraine", "Slow")
    coach2 = Coach("Kadat Uzbekovich", 31, "Uzbekistan", "Smart")

    team.recruit_member(coach1)
    team.recruit_member(coach2)

    # Додавання працівників
    staff1 = Staff("Ilya Monersy", 23, "Ukraine", "Аналітик")

    team.recruit_member(staff1)

    # Участь у турнірі
    print()
    tournament = tournaments[0]
    tournament.participate_tournament(team)
    print("Всі учасники турніру:")
    print(tournament.teams)
    print()

    # Прибрання участі у турнірі
    tournament.leave_tournament(team)
    print("Оновлений список учасників турніру:")
    print(tournament.teams)
    print()

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

    # Отримання всіх працівників
    print("Всі працівники команди:")
    for staff in team.get_all_staff_members():
        print(staff)
    print()

    # Виведення інформації про спонсора
    print(f"Спонсор команди: {team.sponsor}")
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
        team.recruit_member("Це не об'єкт TeamMember")
    except TypeError as e:
        print(f"Помилка: {e}")

    while True:
        try:
            print_menu()
            number = int(input("Введіть функцію."))
            if number == 1:
                team_name = input("Введіть назву команди.")
                if team_name == "":
                    raise ValueError("Назва не може бути пустою.")

                game_category = input("Введіть ігрову категорію команди.")
                if game_category == "":
                    raise ValueError("Категорія не може бути пустою.")

                teams.append(Team(team_name, game_category))
            if number == 2:
                try:
                    team = get_team(teams)
                    if not team:
                        continue
                    print(f"Команда: {team.name} | Кількість учасників команди: {len(team.members)}\n")

                    member_type = input("Введіть тип учасника. [player/coach/staff]")

                    member_name = input("Введіть ім'я учасника.")
                    if member_name == "":
                        raise ValueError("Ім'я учасника не може бути пустим.")

                    member_age = int(input("Введіть вік учасника."))
                    if member_age < 14 or member_age > 50:
                        raise ValueError("Вік учасника не підходить для цієї команди.")

                    member_country = input("Введіть країну учасника.")
                    if member_country == "":
                        raise ValueError("Країна учасника не може бути пустим.")

                    if member_type == "player":
                        member_special = input(
                            "Введіть навик гравця. (Rifler / Low Lane / Sniper / Carry / Upper Lane)")
                        member = Player(member_name, member_age, member_country, member_special)
                    elif member_type == "coach":
                        member_special = input("Введіть стиль тренера. (Slow / Smart / Fast / Furry)")
                        member = Coach(member_name, member_age, member_country, member_special)
                    elif member_type == "staff":
                        member_special = input("Введіть спеціальність працівника. (Аналітик/Психолог)")
                        member = Staff(member_name, member_age, member_country, member_special)
                    else:
                        raise ValueError("Помилка типу учасника. Виберіть з [player/coach/staff]")

                    team.recruit_member(member)
                    print(f"Додано учасника до команди {team.name}!")

                except ValueError as e:
                    print(f"Помилка. {e}\n")
            elif number == 3:
                team = get_team(teams)
                if not team:
                    continue

                print_any(sponsors)

                try:
                    index = int(input("Введіть індекс спонсора."))
                    if index < 1 or index > len(sponsors):
                        raise ValueError("Індекс спонсорів не може бути від'ємним або більшим за кількість спонсорів")

                    sponsor = sponsors[index - 1]
                    print(sponsor)

                    team.negotiate_sponsor(sponsor)
                except ValueError as e:
                    print(f"Помилка. {e}\n")

            elif number == 4:
                print_any(tournaments)

                try:
                    index = int(input("Введіть індекс турніру."))
                    if index < 1 or index > len(tournaments):
                        raise ValueError("Індекс турнірів не може бути від'ємним або більшим за кількість турнірів")

                    tournament = tournaments[index - 1]
                    print()
                    print(tournament)

                    team = get_team(teams)
                    if not team:
                        continue

                    if team in tournament.teams:
                        raise ValueError("Ваша команда вже має участь на цьому турнірі.")

                    tournament.participate_tournament(team)
                    print(f"Вашу команду додано до турніру: {tournament.name}!")
                except ValueError as e:
                    print(f"Помилка. {e}\n")
            elif number == 5:
                print_any(tournaments)
                try:
                    index = int(input("Введіть індекс турніру."))
                    if index < 1 or index > len(tournaments):
                        raise ValueError("Індекс турнірів не може бути від'ємним або більшим за кількість турнірів")

                    tournament = tournaments[index - 1]
                    print()
                    print(tournament)

                    team = get_team(teams)
                    if not team:
                        continue

                    if not team in tournament.teams:
                        raise ValueError("Ваша команда не має участі на цьому турнірі.")

                    tournament.leave_tournament(team)
                    print(f"Вашу команду видалено з турніру!")
                except ValueError as e:
                    print(f"Помилка. {e}\n")
            elif number == 6:
                team = get_team(teams)
                if not team:
                    continue

                if not team.sponsor:
                    raise ValueError("Ваша команда не має спонсора")

                team.remove_sponsor()
            elif number == 7:
                print("Список команд: ")
                print_any(teams)
            elif number == 8:
                print("Список турнірів: ")
                print_any(tournaments)
            elif number == 9:
                print("Список спонсорів: ")
                print_any(sponsors)
            elif number == 10:
                team = get_team(teams)
                if not team:
                    continue

                res = None

                param_name = input("Введіть назву параметра. [age/country/name]")
                if param_name == "age":
                    try:
                        age = int(input("Введіть шуканий вік."))
                        if age < 14 or age > 50:
                            raise ValueError("Цей вік за межею допустимого")

                        res = team.search_by_age(age)
                    except ValueError as e:
                        print(e)
                elif param_name == "name":
                    name = input("Введіть шукане ім'я")
                    res = team.search(name)
                elif param_name == "country":
                    country = input("Введіть шукану країну")
                    res = team.search(country)
                else:
                    raise ValueError("Помилка. Виберіть назву з показаних.")

                print_any(res)
            elif number == 11:
                print_any(tournaments)
                try:
                    index = int(input("Введіть індекс турніру."))
                    if index < 1 or index > len(tournaments):
                        raise ValueError("Індекс турнірів не може бути від'ємним або більшим за кількість турнірів")

                    tournament = tournaments[index - 1]
                    print()
                    print(tournament)

                    print_any(tournament.teams)
                except ValueError as e:
                    print(e)
            elif number == 12:
                team = get_team(teams)
                if not team:
                    continue

                print(f"Команда: {team.name}")
                print(f"Категорія команди: {team.game}")
                print(f"Спонсор команди: {team.sponsor}\n")

                print(f"Поточний турнір команди: {find_team_in_tournament(tournaments, team)}\n")

                print("Гравці команди: ")
                print_any(team.get_all_players())

                print("Тренера команди: ")
                print_any(team.get_all_coaches())

                print("Працівники команди: ")
                print_any(team.get_all_staff_members())


        except ValueError as e:
            print(e)
        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    main()