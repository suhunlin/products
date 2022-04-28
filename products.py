import os
def user_input(products):
    while True:
        name = input('請輸入商品名稱(\'q\'離開程式):')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        products.append([name,price])
    return products

def load_product(filename):
    products = []
    try:
        with open(filename,'r',encoding='utf-8') as file:
            for line in file:
                if '商品,價格' in line:
                    continue
                name,price = line.strip().split(',')
                products.append([name,price])
    except Exception as error_message:
        print(error_message)
    return products

def store_prodect(products,filename):
    result = False
    if not products:
        print('No products!!!')
        return result
    elif not filename:
        print('No filename!!!')
        return result
    try:
        with open(filename,'w',encoding='utf-8') as file:
            file.write('商品' + ',' + '價格' + '\n')
            for project in products:
                file.write(project[0] + ',' + project[1] + '\n')
            result = True
    except Exception as error_message:
        print(error_message)
    return result

def print_product_info(products):
    if not products:
        print('沒有任何產品資訊!!!')
    for product in products:
        print(product[0],',',product[1])

def main():
    filename = 'products.csv'
    if os.path.exists(filename):
        products = load_product(filename)
    else:
        products = []
    products = user_input(products)
    print_product_info(products)
    if store_prodect(products, filename):
        print('save file success!!!')
    else:
        print('save file false!!!')

if __name__ == '__main__':
    main()