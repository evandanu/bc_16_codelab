class lady(object):
    def __init__(self,name,age,height_in_cm,weight_in_kgs):
        self.name=name
        self.age=age
        self.height_in_cm=height_in_cm
        self.weight_in_kgs=weight_in_kgs

    def bmi(self):
        bmi= self.weight_in_kgs / (self.height_in_cm*self.height_in_cm)
        return bmi

    def calories_to_maintain_current_weight(self,activity_factor):
        self.activity_factor=activity_factor
        calories=((655+(9.6*self.weight_in_kgs)+(1.8*self.height_in_cm)-(4.7*self.age))*self.activity_factor)
        return calories

    def nutrition_calculator(self,fats,carbohydrates,proteins):
        self.fats=fats
        self.carbohydrates=carbohydrates
        self.proteins=proteins

        nutrition= ((self.fats*9)+(self.carbohydrates*4)+(self.proteins*4))
        return nutrition

    def menses(self, cycle_days,first_day_of_menses):
        self.cycle_days=cycle_days
        self.first_day_of_menses=first_day_of_menses

        day_of_expecting_menses=(first_day_of_menses+self.cycle_days)
        return day_of_expecting_menses
