import pyinputplus as pyip
bread = {"wheat":50, "white":40, "sourdough":60}
protein = {"chicken":60, "turkey":70, "ham":80, "tofu":50}
cheese = {"cheddar":40, "swiss":50, "mozzarella":60}
topping = {"mayo":20, "mustard":20, "lettuce":15, "tomato":15}

price = 0

print("what type of bread do you want?")
breado = pyip.inputMenu(["wheat", "white", "sourdough"])
print("what protein do you want?")
proteino = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"])
print("would you like cheese?")
response = pyip.inputYesNo()  
print("would you like any toppings?")
response2 = pyip.inputYesNo()

price += bread[breado] + protein[proteino]

if response == "yes":
    print("what cheese would you like?")
    cheeseo = pyip.inputMenu(["cheddar", "swiss", "mozzarella"])  
    price += cheese[cheeseo]




if response2 == "yes":
    print("what toppings would you like?")
    toppingo = pyip.inputMenu(["mayo", "mustard", "lettuce", "tomato"])
    price += topping[toppingo]

print("how many sandwiches do you need?")
response3 = pyip.inputInt(blockRegexes=[r'[1]'])

price = response3*price

print("the total price is: ", price)

  
    
