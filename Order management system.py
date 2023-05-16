from equipment import Equipment
from warehouse import Warehouse


class Recipe:
    def __init__(self, ingredients: dict[str: float], cooking_sequence: dict[str: str]):
        self.ingredients = ingredients
        self.cooking_sequence = cooking_sequence

    def get_ingredients(self):
        return self.ingredients

    def get_cooking_sequence(self):
        return self.cooking_sequence

class Pizza:
    def __init__(self, name: str, size: float, recipe: Recipe, thickness: int = 4, additions: dict[str: float] = None):
        self.name = name
        self.size = size
        self.recipe = recipe
        self.thickness = thickness
        self.additions = additions
        self.price = None

    def add_ingredients(self, ingredients: dict[str: int]):
        for ingr, amount in ingredients.items():
            if ingr not in self.recipe.ingredients:
                self.recipe.ingredients[ingr] = amount
            else:
                self.recipe.ingredients[ingr] += amount

    def remove_ingredients(self, ingredients: dict[str: int]):
        for ingr, amount in ingredients.items():
            if ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] > amount:
                self.recipe.ingredients[ingr] -= amount
            elif ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] == amount:
                del self.recipe.ingredients[ingr]
            elif ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] < amount:
                print('Deliting is unavaible')
                return 0
            else:
                print(f'Deliting is unavaible. Did\'n found \"{ingr}\"')
                return 0

class Drink:
    def __init__(self, name: str, recipe: Recipe, additions: dict[str: float] = None):
        self.name = name
        self.size = None
        self.recipe = recipe
        self.additions = additions
        self.price = None

    def add_ingredients(self, ingredients: dict[str: int]):
        for ingr, amount in ingredients.items():
            if ingr not in self.recipe.ingredients:
                self.recipe.ingredients[ingr] = amount
            else:
                self.recipe.ingredients[ingr] += amount

    def remove_ingredients(self, ingredients: dict[str: int]):
        for ingr, amount in ingredients.items():
            if ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] > amount:
                self.recipe.ingredients[ingr] -= amount
            elif ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] == amount:
                del self.recipe.ingredients[ingr]
            elif ingr in self.recipe.ingredients and self.recipe.ingredients[ingr] < amount:
                print('Deliting is unavaible')
                return 0
            else:
                print(f'Deliting is unavaible. Did\'n found \"{ingr}\"')
                return 0

class Menu:
    def __init__(self):
        self.pizzas: list[Pizza] = []
        self.drinks: list[Drink] = []

    def make_choice(self, warehouse):
        end_choice = [[], []]
        while True:
            choice = input("What do u want?\n1. Coffee\n2. Pizza\n3. Exit\nAnswer: ")
            if choice == 'Coffee' or choice == "1":
                print('Which coffee do you want?')
                if len(self.drinks) == 0:
                    print("We've no coffee yet.")
                    continue
                for i in range(len(self.drinks)):
                    print(str(i+1)+". \"" + self.drinks[i].name + "\"")
                choice = input("Answer(name): ")
                choice_size = input("Какого размера?(стандарт/большой): ")
                end_choice[0].append([choice, choice_size])
                continue
            elif choice == 'Pizza' or choice == "2":
                print('Which pizza do you want?')
                if len(self.pizzas) == 0:
                    print("We've no pizza yet.")
                    continue
                for i in range(1, len(self.pizzas)):
                    print(str(i+1)+". \"" + self.pizzas[i].name + "\"")
                choice = input("Answer(name): ")
                choice_size = input("Какого размера?(стандарт/большая): ")
                end_choice[0].append([choice, choice_size])
                end_choice[1].append(choice)
                continue
            elif choice == 'Exit' or choice == "3":
                break
        return end_choice

coff_machine1 = Equipment("Кофе машина", "Свободна", True)

menu = Menu()

menu.drinks.append(Drink("Эспрессо", Recipe({'кофе': 8.5}, {'темпер': 'прессовать'})))
menu.drinks.append(Drink("Американо", Recipe({'кофе': 9, 'вода': 250}, {'темпер': 'прессовать', 'чайник':"добавить воды"})))
menu.drinks.append(Drink("Латте", Recipe({'кофе': 0.3, 'молоко': 0.6}, {'кофе машина': 'подогреть', "стакан": "перелить молоко"})))


for drink in menu.drinks:
    print(drink.name, drink.size, drink.recipe.ingredients)


warehouse = Warehouse()
warehouse.add_product({'кофе': 0.3, 'молоко': 0.6})


make_choice = menu.make_choice(warehouse)
if len(make_choice[0]) > 0 or len(make_choice[1]) > 0:
    for i in range(len(make_choice[0])):
        print("We are doing ur", make_choice[0][i])
    for i in range(len(make_choice[1])):
        print("We are doing ur", make_choice[1][i])
else:
    print("U didnt do your order;(")