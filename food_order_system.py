#Training Python
#Food order system - Dictionnary
italian_food = [
    "Pasta Bolognese",
    "Pizza",
    "Risotto"
]

french_food = [
    "Baguette",
    "Crêpe",
    "Fromage"
]

def find_meal(name, menu):
    return name if name in menu else None
def select_meal(name, food_type):
    if food_type == "Italian":
        return find_meal(name, italian_food)
    elif food_type == "French":
        return find_meal(name, french_food)
    else:
        return None

def display_available_meals(food_type):
    if food_type == "Italian":
        print("Available Italian Meals:")
        for meal in italian_food:
            print(meal)

    elif food_type == "French":
        print("Available French Meals:")
        for meal in french_food:
            print(meal)

    else:
        print("Invalid food type")

def create_summary(name, amount, food_type):
    order = select_meal(name, food_type)
    if order:
        return f"You order {amount} {name}"
    else:
        return "Meal not found"
print("Welcome to the Food Order System!")
type_input = input("What type of food to you want? ")
display_available_meals(type_input)

name_input = input("Enter the order: ")
amount_input = input("How much do you want? ")

result = create_summary(name_input, amount_input, type_input)
print(result)