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

    def get_cost(self):
        '''return cost value'''
        return self.price / self.weight

def knapsack(items, capacity):
    '''knapsack'''

    weight = 0
    price = 0
    item_arr = sorted(items, key=lambda x: x.get_cost(), reverse=True)

    print("Knapsack Size: %.1f kg"  % (capacity))
    print("===============================")
    for i in item_arr:
        if weight + i.get_weight() <= capacity:
            weight += i.get_weight()
            price += i.get_price()
            print(i.get_name() + " -> " + str(i.get_weight()) + " kg -> " + \
                   str(i.get_price()) + " THB")
        else:
            break

    print("Total: %d THB" % int(price))



def main():
    '''main function'''
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(
            Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)

main()
