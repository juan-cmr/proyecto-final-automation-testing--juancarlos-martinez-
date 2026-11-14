import csv


def read_users_csv():
    with open("data/users.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)
