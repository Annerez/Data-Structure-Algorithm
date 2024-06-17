"""asd"""

import json

def coin(amt, max_coin):
    """asdas"""
    ans = ["10 baht = 0 coins", "5 baht = 0 coins", "2 baht = 0 coins", "1 baht = 0 coins"]
    count = 0
    print("Amount:", amt)
    while True:
        if amt <= 0:
            print("Coin exchange result:")
            for result in ans:
                print(" ", result)
            print("Number of coins:", count)
            break
        if amt > 0 and max_coin["10"] <= 0 and max_coin["5"] <= 0 \
            and max_coin["2"] <= 0 and max_coin["1"] <= 0:
            print("Coins are not enough.")
            break

        for i, coin_value in enumerate([10, 5, 2, 1]):
            if amt >= coin_value and max_coin[str(coin_value)] > 0:
                num_coins = min(amt // coin_value, max_coin[str(coin_value)])
                ans[i] = str(coin_value) +" baht = " + str(num_coins) + " coins"
                count += num_coins
                amt -= num_coins * coin_value
                max_coin[str(coin_value)] -= num_coins

coin(int(input()), json.loads(input()))

