
def sorte_product(product_list):
    try:
        with open('products.csv','w',encoding='utf-8') as file:
            file.write('產品'+','+'價格'+'\n')
            for product in product_list:
                file.write(product[0]+','+product[1]+'\n')

    except Exception as error_message:
        print(error_message)

def load_product():
    products = []
    try:
        with open('products.csv','r',encoding='utf-8') as file:
            for line in file:
                if '產品,價格' in line:
                    continue
                name,price = line.strip().split(',')
                products.append([name,price])
    except Exception as error_message:
        print(error_message)
    return products

def user_input_product(product_list):
    products = product_list
    while True:
        name = input('請輸入產品名稱(結束輸入q):')
        if name == 'q':
            if not products:
                print('No product data!!!')
            else:
                sorte_product(products)
            break
        price = input('請輸入產品價格：')
        products.append([name,price])

def main():
    products = load_product()
    print(products)
    user_input_product(products)

if __name__ == '__main__':
    main()