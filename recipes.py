class Recipes:
    # класс рецептов, что содержит в себе массивы с ингредиентами и способом приготовления
    # ингредиенты - словать, в котором ключ - это название ингридиента, а значение - количество
    # способом приготовления - словарь, в котором ключ - это на чем делать, а значение - что делать
    def __init__(self, ingredients: dict[str: float], cooking_sequence: dict[str: str]):
        self.ingredients = ingredients
        self.cooking_sequence = cooking_sequence

    def get_ingredients(self):
        return self.ingredients

    def get_cooking_sequence(self):
        return self.cooking_sequence #


class Eat:
    # класс еды с методами её изменения или добавления(рецептов и способов приготовления)
    def __init__(self, name: str, size: float, recipe: Recipes, price: float = None):
        self.name = name
        self.size = size
        self.recipe = recipe
        self.price = price
        self.additive_list = []

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def set_size(self, size: str):
        self.size = size

    def get_size(self):
        return self.size

    def set_price(self, price: float):
        self.price = price

    def get_price(self):
        return self.price

    def set_recipe(self, recipe: Recipes):
        self.recipe = recipe

    def get_recipe(self):
        return self.recipe

    def get_ingredients(self):
        return self.recipe.ingredients

    def get_cooking_sequence(self):
        return self.recipe.cooking_sequence

    def ingredient_in_recipe(self, additive: str):
        for ingredient in self.recipe.ingredients:
            if additive == ingredient:
                return True
        return False

    def add_additive(self, additive_list: list):
        for additive in additive_list:
            if self.ingredient_in_recipe(additive):
                user_input = input("Хотите больше продукта \"" + str(additive) + "\"? (Да/Нет): ")
                if user_input == "Да":
                    self.recipe.ingredients[additive] *= 2
                    self.additive_list.append(additive)
            else:
                self.recipe.ingredients[additive] = 1
                self.additive_list.append(additive)

    def remove_additive(self, additive_list: list):
        for additive in additive_list:
            if self.ingredient_in_recipe(additive):
                del self.recipe.ingredients[additive]
                self.additive_list.remove(additive)


class Coffee(Eat):
    def __init__(self, name: str, size: float, recipe: Recipes, price: float = None):
        super().__init__(name, size, recipe, price)
        self.additive_list = []

    def get_info(self):
        ingredient_str = ''
        ingredients_list = self.get_ingredients()
        ingredients_list = set(ingredients_list)
        for ingredient in ingredients_list:
            ingredient_str += ingredient + ", "
        ingredient_str = ingredient_str[:-2]
        return f'Название кофе: {self.name}, размер кофе - {self.size}л.\nИз чего состоит кофе: {ingredient_str}'


class Pizza(Eat):
    def __init__(self, name: str, size: float, recipe: Recipes, price: float = None):
        super().__init__(name, size, recipe, price)
        self.additive_list = []

    def get_info(self):
        ingredient_str = ''
        ingredients_list = self.get_ingredients()
        ingredients_list = set(ingredients_list)
        for ingredient in ingredients_list:
            ingredient_str += ingredient + ", "
        ingredient_str = ingredient_str[:-2]
        ingredient_str += "."
        return f'Название пиццы: {self.name}, размер пиццы - {self.size}мм в диаметре.\nИз чего состоит пицца: {ingredient_str}'
