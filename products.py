
products = []
def load_function():
    try:
        with open('product.csv', 'r', encoding='utf-8') as file:
            for line in file:
                if '商品,價格' in line:
                    continue #繼續
                name, price = line.strip().split(',') #1.先用strip把讀到的資料\n刪掉2.再用split(',')把資料依照','分隔
                                                      # 3.把分隔後的資料分別存到name跟price裡
                products.append([name,price])
        print(products)
    except Exception as error_message:
        print(error_message)

def store_function(list_data):
    try:
        with open('product.csv','w',encoding='utf-8') as file:
            file.write('商品' + ',' + '價格'+'\n')
            for product in list_data:
                file.write(product[0] + ',' + product[1]+'\n')
    except Exception as error_message:
        print(error_message)

def main():
    load_function()
    while True:
        product = input('請輸入商品名稱(結束請輸入q):')
        if product == 'q':
            if not products:  # 如果products list裡面是空清單的話
                print('空清單，離開!!!')
                break
            else:
                store_function(products)
            break
        price = input('請輸入商品價格:')
        products.append([product, price])
if __name__ == '__main__':
    main()




