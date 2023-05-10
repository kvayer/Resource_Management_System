from recipes import Pizza, Recipes

if __name__ == '__main__':
    pizza1 = Pizza('пепирони', 'средняя', Recipes(["лук", "сыр", "грибы", "ветчина"],
                                                  ["подготовить тесто", "разрезать ингридиенты",
                                                   "разместить ингридиенты на тесто", "запечь на 40 минут"]))
    print(pizza1.get_pizza_name(), pizza1.get_pizza_size(), pizza1.recipe.ingredients)
    pizza1.add_additive('ананас')
    print(pizza1.get_pizza_name(), pizza1.get_pizza_size(), pizza1.recipe.ingredients)
    pizza1.remove_additive("лук")
    print(pizza1.get_pizza_name(), pizza1.get_pizza_size(), pizza1.recipe.ingredients)
    pizza1.add_additive('ананас')
    print(pizza1.get_pizza_name(), pizza1.get_pizza_size(), pizza1.recipe.ingredients)