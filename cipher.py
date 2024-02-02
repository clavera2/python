card_number = (input("Enter 6 digits card number: "))
if len(card_number) != 6:
    print("Error! length of card number is not 6")
else:
    card_number = list(card_number)
    card_number[0] = "*"
    card_number[1] = "*"
    card_number[2] = "*"
    card_number[3] = "*"
    print(card_number)