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
    def __init__(self, name: str, size: float, recipe: Recipe, additions: dict[str: float] = None):
        self.name = name
        self.size = size
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

    def make_choice(self):
        end_choice = [[], []]
        while True:
            choice = input("What do u want?\n1. Coffe\n2. Pizza\n3. Exit\nAnswer: ")
            if choice == 'Coffee' or choice == "1":
                print('Which coffee do you want?')
                if len(self.drinks) == 0:
                    print("We've no coffe yet.")
                    continue
                for i in range(len(self.drinks)):
                    print(str(i+1)+". \"" + self.drinks[i].name + "\" - ", self.drinks[i].size, end='\n')
                choice = input("Answer(name): ")
                end_choice[0].append(choice)
                continue
            elif choice == 'Pizza' or choice == "2":
                print('Which pizza do you want?')
                if len(self.pizzas) == 0:
                    print("We've no pizza yet.")
                    continue
                for i in range(1, len(self.pizzas)):
                    print(str(i+1)+". \"" + self.pizzas[i].name + "\" - ", self.pizzas[i].size, end='\n')
                choice = input("Answer(name): ")
                end_choice[1].append(choice)
                continue
            elif choice == 'Exit' or choice == "3":
                break
        return end_choice



menu = Menu()

menu.drinks.append(Drink("Hui", 0.5, Recipe({'per': 1, 'vtoroi': 2}, {'just_do': 'ok'})))
menu.drinks.append(Drink("Pizda", 1, Recipe({'per': 1, 'vtoroi': 2}, {'just_do': 'ok'})))
menu.drinks.append(Drink("Chelovek", 0.7, Recipe({'per': 1, 'vtoroi': 2}, {'just_do': 'ok'})))
menu.pizzas.append(Pizza("Пеперони", 0.5, Recipe({'перец': 1, 'тесто': 2}, {'just_do': 'ok'})))

# for drink in menu.drinks:
#     print(drink.name, drink.size, drink.recipe.ingredients)
#
# make_choice = menu.make_choice()
# if len(make_choice[0]) > 0 or len(make_choice[1]) > 0:
#     for i in range(len(make_choice[0])):
#         print("We are doint ur", make_choice[0][i])
#     for i in range(len(make_choice[1])):
#         print("We are doint ur", make_choice[1][i])
# else:
#     print("U didnt do your order;(")

print(menu.pizzas[0].recipe.ingredients)
menu.pizzas[0].add_ingredients({'перец': 8, "тесто": 3, "грибы": 1})
print(menu.pizzas[0].recipe.ingredients)
menu.pizzas[0].remove_ingredients({'перец': 8, "тесто": 3, "грибы": 1})
print(menu.pizzas[0].recipe.ingredients)
menu.pizzas[0].remove_ingredients({"грибы": 1})