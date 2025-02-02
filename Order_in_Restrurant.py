menu ={
    'pizza' : 40,
    'pasta' : 50,
    'burger' : 60,
    'salad' : 30,
    'coffee' : 25,
    'tea' : 15,
}

print('Welcome to Zangetsu Restrurent, Sir!!\n')

print('Pizza : 40 TK\nPasta : 50 TK\nBurger : 60 TK\nSalad : 30 TK \nCoffee : 25 TK \nTea : 15 TK')

order_total = 0
food = []

item_1 = input('Enter the name of the food you want to order: ')
item_1 = item_1.lower()
quantity = int(input('Quantity of order: '))

if item_1 in menu:
    food.append(item_1)
    order_total += menu[item_1] * quantity
    print(f'Your item {item_1} has been added to the order list.')

else:
    print(f'{item_1} is not in our menu. \nPlease order Something that we can serve you.')

for i in range(5):
    next_item = input('Do you want to add another product in the list? (Yes / No): ')
    next_item = next_item.lower()
    if next_item == "yes":
        item_2 = None
        quantity = None
        item_2 = input('Enter the name of the food you want to order: ')
        item_2 = item_2.lower()
        quantity = int(input('Quantity of order: '))

        if item_2 in menu:
            food.append(item_2)
            order_total += menu[item_2] * quantity
            print(f'Your item {item_2} has been added to the order list.')
        else:
            print(f'{item_2} is not in our menu. \nPlease order Something that we can serve you.')

    else:
        break

print(f'Your order list is {food}')
print(f'The ammount to pay = {order_total}. ')
