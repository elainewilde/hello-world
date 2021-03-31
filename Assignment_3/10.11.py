#Elaine Wilde 1671617

class FoodItem:

    def __init__(self, food_name="None", num_fat=0, num_carbohydrates=0, num_protein=0, num_servings=0):
        self.name = food_name
        self.fat = num_fat
        self.carbs = num_carbohydrates
        self.protein = num_protein
        self.num_servings = num_servings

        self.print_info()


    def get_calories(self, num_servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print("Number of calories for {:.2f}".format(self.num_servings)+ " serving(s): {:.2f}".format(self.get_calories(self.num_servings)))

if __name__ == '__main__':
    food_name = input()
    num_fats = float(input())
    asdf=float(input())
    num_prot=float(input())
    num_serv=float(input())

    FoodItem("None",0,0,0,num_serv)
    print()
    FoodItem(food_name,num_fats,asdf,num_prot,num_serv)

