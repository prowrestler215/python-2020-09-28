# How a Few Undersea Cables Connect the Entire Internet
# https://www.youtube.com/watch?v=eTBLIYJSzdc

# OOP

# classes
# attributes
# methods
# chaining
# association between classes

# Mammals, cats, dogs

cat_name = 'Felix'
cat_age = 3

cat_name1 = 'Sunny'
cat_age1 = 5

cat_obj = {
    'name': 'Felix',
    'age': 3,
}

cat_obj1 = {
    'name': 'Sunny',
    'age': 5,
}

# blueprint
class Cat:
    def __init__(self, name_parameter, age_parameter):
        print('Initializing a Cat instance!')
        self.name = name_parameter
        self.age = age_parameter
        self.health = 100

    def meow(self):
        print(f'{self.name} made a Meow! 😸')
        return self

    def claw_another_cat(self, instance_of_enemy_cat):
        # remove 10 health from the other cat
        instance_of_enemy_cat.health -= 10
        print(f'{instance_of_enemy_cat.name} took damage!')
        print(f'Health is now: {instance_of_enemy_cat.health}')
        return self

    def purrr(self):
        # increases our health + 10
        self.health += 10
        print(f'{self.name} now has a health of {self.health}')
        return self


# create an instance of a cat
instance_of_cat0 = Cat('Felix', 3)
# check out some of the attributes
print(instance_of_cat0)
print(instance_of_cat0.name)
print(instance_of_cat0.age)
# test out some of the methods
instance_of_cat0.meow()
print('**************************')

instance_of_cat1 = Cat('Sunny', 5)
print(instance_of_cat1)
print(instance_of_cat1.name)
print(instance_of_cat1.age)
instance_of_cat1.meow()
instance_of_cat1.purrr().purrr()

instance_of_cat0.claw_another_cat(instance_of_cat1)
