#calculator project
class Calculator(object):
    "calculator"
    #init metodu
    def __init__(self,a,b):
        "initialize values"
        #attribute
        self.value1 = a
        self.value2 = b
        
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
     

    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
    def subtraction(self):
        "subtraciton a-b = result -> return result"
        return self.value1-self.value2
print("Choose add(1), multiply(2), division(3), subtraction(4)")
selection = input("select 1 , 2 ,3 or 4 ")
v1 = int(input("first value : "))
v2 = int(input("second value : "))
c1 = Calculator(v1, v2)
if selection == "1":
   add_result = c1.add()
   print("Add : {}".format(add_result))
elif selection == "2":
   multiply_result = c1.multiply()
   print("Multiply: {}".format(multiply_result))
elif selection == "3":
    division_result = c1.division()
    print("Division: {} ".format(division_result))
elif selection == "4":
    subtraciton_result = c1.subtraction()
    print("Subtraction: {} ".format(subtraciton_result))
else: 
    print("ERROR!!!")