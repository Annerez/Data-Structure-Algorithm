'''Item Classes'''

class Item:
    '''Items'''

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        '''return name'''
        return self.name

    def get_price(self):
        '''return price'''
        return self.price

    def get_weight(self):
        '''return weight'''
        return self.weight

def main():
    '''main function'''
    import json
    item_in = json.loads(input())
    item = Item(item_in["name"], item_in["price"], item_in["weight"])
    print(item.get_name(), item.get_price(), item.get_weight(), sep='\n')

main()
