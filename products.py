products = []
def save_function(products_data):
    try:
        with open("product.txt","w") as file:
            for product in products_data:
                str = product[0] + "," + product[1] + "\n"
                file.write(str)
    except Exception as error_message:
        print(error_message)
while True:
    name = input("Please input product name(press q to exit):")
    if name == "q":
        print(products)
        save_function(products)
        break
    price = input("Please input product price:")
    # p = [name,price]
    products.append([name,price])




