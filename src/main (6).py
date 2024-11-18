#The Coffee Shop Price Calculator - www.101computing.net/the-coffee-shop-price-calculator

Coffee = {"espresso", "americano", "latte", "cappuccino", "macchiato", "mocha", "flat"}


print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+         The Coffee Shop       +")
print("+              Welcome          +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat white")
print("----------------------------")

price = 0
want = input("What type of coffee would you like? (Flat white = Flat) ").lower()
while want not in Coffee:
 want = input("Not in list, please enter coffee name again")
if want =="espresso":
   price = price + 2.50
elif want =="americano":
   price = price + 3
elif want =="latte":
   price = price + 2.50
elif want =="cappuccino":
   price = price + 3.00
elif want =="macchiato":
   price = price + 2.50
elif want =="mocha":
   price = price + 3.50
elif want =="flat":
   price = price + 2.50


size = input("What size would you like? (M/L/XL) ").upper()
while size not in ["M", "L", "XL"]:
   print("Not an option.")
   size = input("What size would you like? (M/L/XL) ").upper()

if size == "L":
   price += 1.00
elif size == "XL":
   price += 1.50

where = input("Would you like to eat in or take away? (yes or no)").lower()
while where != "yes" and where != "no":
   where = input("Not an option. Please choose again: ").lower()
if where == "yes":
   price = price + 1.00


print("----------------------------")
print("Total Cost: £" + str(price))