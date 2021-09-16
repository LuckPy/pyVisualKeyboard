from pprint import pprint
from random import choice


def return_random_text(nb_ligne):  # retourne une liste de lignes aléatoires
    with open("resources/text.txt", "r") as f:
        data = f.read()
        selected_in = [choice(data.replace("\n", "").split(".")) for _ in range(nb_ligne)]
        return [ligne[1:] for ligne in selected_in if ligne[0] == " "]


class SpeedTyping:
    def __init__(self):
        pass


if __name__ == "__main__":
    a = SpeedTyping()
    pprint(return_random_text(6))
