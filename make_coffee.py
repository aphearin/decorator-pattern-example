import coffeeshop

# Below is an example script showing how to use 
# the decorator design pattern 
# to construct objects with complex behavior using 
# composition rather than inheritance

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.getIngredients()+'; Cost: '+str(myCoffee.getCost()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.getIngredients()+'; Cost: '+str(myCoffee.getCost()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.getIngredients()+'; Cost: '+str(myCoffee.getCost()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.getIngredients()+'; Cost: '+str(myCoffee.getCost()))








