
def get_ticket_price():
    ordernumber = int(input("number of zakaz: "))
    standardprice = 2000

    if ordernumber % 1000 == 0:
        return standardprice * 0.8
    else:
        return standardprice


def get_total_price():
    total = 0.0
    while True:
        choice = input("buy bilet? off - stop\n>>> ").lower()
        if choice == "off":
            break
        price = get_ticket_price()
        print(f"one bilet price: {price}")
        total += price
    print(f"total price: {total}")
