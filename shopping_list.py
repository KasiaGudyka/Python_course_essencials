# calculating a cost of shopping in a small grocery store
shopping_list = []
  
# number of elemetns as input 
print("Today in stock:\nbananas,\napples,\noranges,\npears,\n\n")

#initiating a size of a shopping list
n = int(input("Enter number of items in you shopping list: ")) 
  
#  adding items to a shopping list
for i in range(0, n): 
    ele = str(input("Add an item to your shopping list : ")) 
  
    shopping_list.append(ele) 
    
# checking if items are in stock
for i in range(0, len(shopping_list)):
  if shopping_list[i] != "bananas" and shopping_list[i] != "apples" and shopping_list[i] != "oranges" and shopping_list[i] != "pears":
    print("There is no ", shopping_list[i], " in stock")
    shopping_list[i] = "empty"

stock = {
  "bananas": 6,
  "apples": 10,
  "oranges": 32,
  "pears": 15,
  "empty": 0
}
    
prices = {
  "bananas": 4,
  "apples": 2,
  "oranges": 1.5,
  "pears": 3,
  "empty": 0
}

# calculating a bill
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

print("In total your shopping costs: ", str(compute_bill(shopping_list)), " euros")
