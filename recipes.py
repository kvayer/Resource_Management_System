class Recipes:
    def __init__(self, ingredients: list, cooking_sequence: list):
        self.ingredients = ingredients
        self.cooking_sequence = cooking_sequence

    def get_ingredients(self):
        return self.ingredients

    def get_cooking_sequence(self):
        return self.cooking_sequence


class Coffee:
    def __init__(self, name: str, size: str, recipe: Recipes):
        self.name = name
        self.size = size
        self.recipe = recipe

    def get_coffee_name(self):
        return self.name

    def get_coffee_size(self):
        return self.size

    def get_coffee_recipe(self):
        return self.recipe

class Pizza:
    def __init__(self, name: str, size: str, recipe: Recipes):
        self.name = name
        self.size = size
        self.recipe = recipe
        self.additive_list = []
    def get_pizza_name(self):
        return self.name

    def get_pizza_size(self):
        return self.size

    def get_pizza_ingredients(self):
        return self.recipe.ingredients

    def get_pizza_cooking_sequence(self):
        return self.recipe.cooking_sequence

    def ingredient_in_recipe(self, additive: str):
        for ingredient in self.recipe.ingredients:
            if additive == ingredient:
                return False
        return True

    def add_additive(self, additive: str):
        if self.ingredient_in_recipe(additive):
            self.recipe.ingredients.append(additive)
            self.additive_list.append(additive)
        else:
            text = "Хотите двойную порцию " + additive + "? (Y/N): "
            inp = input(text)
            if inp == 'Y':
                text = additive + " x2"
                self.recipe.ingredients.append(text)
                self.additive_list.append(text)
    def remove_additive(self, additive: str):
        if (self.ingredient_in_recipe(additive)):
            return "It is not"
        else:
            if additive in self.additive_list:
                self.additive_list.remove(additive)
                for ingredient in self.recipe.ingredients:
                    if ingredient == additive:
                        self.recipe.ingredients.remove(ingredient)
            else:
                for ingredient in self.recipe.ingredients:
                    if ingredient == additive:
                        self.recipe.ingredients.remove(ingredient)
