class Animals:
    CAT = 0
    DOG = 10
    BIRD = 6
    MICE = None


print(Animals.CAT)
Animals.CAT = 4
print(Animals.CAT)
Animals.WOLF = 9
print(Animals.WOLF)
count = int(input("Input amount of animal: "))
Animals.WOLF = count
print(Animals.WOLF)