def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    full_name = f'{one.title()}{delimiter}{two.title()}'
    return full_name

def format_price(price):
    price = int(price)
    full_price = f'Цена: {price} руб.'
    return full_price

united_name = get_summ('Learn', 'python')
print(united_name)

it_cost = format_price(54)
print(it_cost)

