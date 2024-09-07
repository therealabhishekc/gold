# scrap gold calculations
def scrap_gold(gold_24k, gold_wt, gold_kt, gold_pur_place):
    gold_kt = int(gold_kt[:2])

    if gold_pur_place == "Govindji's":
        price = gold_24k * (gold_kt/24)
        cash = price - 5.5
        trade = price - 4.5
        marker = "*"

    else:
        price_22k = gold_24k * 0.8
        price = price_22k * (gold_kt/22)
        cash = price - 5.5
        trade = price - 4.5
        marker = ""

    return (round(cash * float(gold_wt)), 
            round(trade * float(gold_wt)), 
            marker)


# gold breakdown calculations
def gold_bd(price, gold_wt, gold_22k):
    price, gold_wt = float(price), float(gold_wt)
    price_pre_tax = round(price / 1.0825)
    price_duty = round(price_pre_tax * 0.065)
    price_gold = round(gold_wt * gold_22k)

    remaining = price_pre_tax - price_gold - price_duty
    temp = round(remaining//2)

    if remaining % 2 == 0:
        price_labor, price_profit = temp, temp
    else:
        price_labor, price_profit = temp+1, temp
    
    return price_gold, price_labor, price_profit, price_duty, price_pre_tax


# unique profit for each item_code
def get_profit(s, min_value=8.99, max_value=9.21):
    hash_value = hash(s)
    
    normalized_value = float(hash_value)
    
    scaled_value = min_value + (normalized_value % (max_value - min_value))
    
    return scaled_value


# hyderabadi breakdown calculations
def hyd_bd(price, net_wt, total_stone_ct, gold_22k):
    price = float(price)
    price_pre_tax = round(price / 1.0825)
    price_duty = round(price_pre_tax * 0.065)
    price_gold = round(net_wt * gold_22k)

    profit = 8.50
    while True:
        price_stones = price_pre_tax - price_gold - price_duty - (2 * (profit/100) * price_pre_tax)
        price_per_carat = price_stones/total_stone_ct
        if price_per_carat < 25:
            price_stones = round(price_stones)
            break
        else:
            profit += 0.05 

    price_labor = round((profit * price_pre_tax)/100)
    price_profit = price_pre_tax - price_gold - price_duty - price_stones - price_labor

    return price_gold, price_stones, price_labor, price_profit, price_duty, price_pre_tax
