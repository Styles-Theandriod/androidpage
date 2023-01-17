is_hot = False;
is_cold = False;

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a Cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day!!")


    #Imagin a Price of a house is $1M
    # buyer has good credit
    # they need to put down 10%
    # otherwise
    # they need to put down 20%

    price = 1000000
    has_good_credit = True

    if has_good_credit:
        down_payment = 0.1 * price
    else:
        down_payment = 0.2 * price
    print(f'Down payment: {down_payment}')
