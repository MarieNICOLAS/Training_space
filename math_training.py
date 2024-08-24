import math
import random

def validation(message):
    choice = True
    user_choice = input(f"{message} ? O / N ")
    if user_choice == "O":
        choice = True
        return choice
    elif user_choice == "N":
        choice = False
        return choice
    else:
        print("Erreur de saisie")
        return validation("Ressaisir la réponse")

def training_addition():
    user_choice = True
    score = 0
    while user_choice:
        number_1 = random.randint(0, 250)
        number_2 = random.randint(0, 250)
        print(f"Calculer {number_1} + {number_2}")
        answer = int(input("Réponse: "))
        if answer == number_1 + number_2:
            print("Vrai !")
            score +=1
            print(f"Score = {score}")
            user_choice = validation("Continuer")
        else:
            print("Faux!")
            print(f"Réponse = {number_1} + {number_2} = {number_1 + number_2}")
            print(f"Score = {score}")
            user_choice = validation("Continuer")

def training_soustraction():
    user_choice = True
    score = 0
    while user_choice:
        number_1 = random.randint(0, 250)
        number_2 = random.randint(0, 250)
        print(f"Calculer {number_1} - {number_2}")
        answer = int(input("Réponse: "))
        if answer == number_1 - number_2:
            print("Vrai !")
            score +=1
            print(f"Score = {score}")
            user_choice = validation("Continuer")
        else:
            print("Faux!")
            print(f"Réponse = {number_1} - {number_2} = {number_1 - number_2}")
            print(f"Score = {score}")
            user_choice = validation("Continuer")

def training_multiplication():
    user_choice = True
    score = 0
    while user_choice:
        number_1 = random.randint(1, 10)
        number_2 = random.randint(1, 10)
        print(f"Calculer {number_1} * {number_2}")
        answer = int(input("Réponse: "))
        if answer == number_1 * number_2:
            print("Vrai !")
            score +=1
            print(f"Score = {score}")
            user_choice = validation("Continuer")
        else:
            print("Faux!")
            print(f"Réponse = {number_1} * {number_2} = {number_1 * number_2}")
            print(f"Score = {score}")
            user_choice = validation("Continuer")

def table_multiplication(number):
    while user_choice:
        print(f"Table de {number}")
        for i in range(1, 11):
            answer = number * i
            print(f"{number} * {i} = {answer}")
        user_choice = validation("Nouvelle table de multiplication")

user_choice = True
while user_choice:
    print("1: Addition")
    print("2: Soustraction")
    print("3: Multiplication")
    print("4: Tables de Multiplication")
    choice = int(input("Choisir l'entrainement: "))

    if choice == 1:
        print("Addition")
        training_addition()
        user_choice = validation("Retour au menu")
    elif choice == 2:
        print("Soustraction")
        training_soustraction()
        user_choice = validation("Retour au menu")
    elif choice == 3:
        print("Multiplication")
        training_multiplication()
        user_choice = validation("Retour au menu")
    elif choice == 4:
        print("Table de multiplication")
        number = int(input("Entrer la table de multiplication: "))
        table_multiplication(number)
        validation("Retour au menu")
    else:
        run = False