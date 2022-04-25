products = []
while True:
    name = input("Please input product name:")
    if name == "q":
        break
    price = input("Please input product price:")
    # p = [name,price]
    products.append([name,price])
for product in products:
    str = '商品名稱：'+product[0]+',商品價格：'+product[1]
    print(str)



try:
    with open('products.txt','w') as file:
        for product in products:
            str = "商品名稱："+product[0]+",商品價格："+product[1]+"\n"
            file.write(str)

except Exception as e:
    print(e)
