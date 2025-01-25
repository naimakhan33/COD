#define the menu of resturant
menu ={
    'pizza':40,
    'cake':50,
    'burger':100,
    'pasta': 60,
    'salad':70,
    'coffee':80,
    'baryani': 50,

}
#greet
print("Welcome to our resturant:")
print("pizza: Rs40\ncake :Rs 50\nburger: Rs 100\npasta:Rs60\nsalad : Rs 70\ncoffee: Rs 80\nbaryani: Rs50")

order_total = 0
#40+50 = 90

item_1 = input("Enter the name of item you want to order:")
if item_1 in menu:
    order_total += menu[item_1] #0 +40
    print(f"uour item{item_1} has been added to your order:")

else:
    print(f"plz order something else we can serve you:")

another_item = input("do you want to another item? (yes/no)")
if another_item == "yes":
    item_2 = input("Enter the name of 2nd item:")
    order_total += menu[item_2] #0 +50
    print(f"uour item{item_2} has been added to your order:")

else:
    print(f"plz order something else we can serve you:")

print(f"The total amount of items to pay is {order_total}")

