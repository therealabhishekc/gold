import random

# scrap gold calculations
def scrap_gold(gold_24k, gold_wt, gold_kt, gold_pur_place):
    gold_kt = int(gold_kt[:2])

    if gold_kt == 24:
        cash = gold_24k * 0.97
        trade = gold_24k
        marker = " " 

    else:
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
# def hyd_bd(price, net_wt, total_stone_ct, gold_22k):
#     price = float(price)
#     price_pre_tax = round(price / 1.0825)
#     price_duty = round(price_pre_tax * 0.065)
#     price_gold = round(net_wt * gold_22k)

#     profit = 8.51
#     while True:
#         price_stones = price_pre_tax - price_gold - price_duty - (2 * (profit/100) * price_pre_tax)
#         price_per_carat = price_stones/total_stone_ct
#         if price_per_carat < 25:
#             price_stones = round(price_stones)
#             break
#         else:
#             profit += 0.05 

#     price_labor = round((profit * price_pre_tax)/100)
#     price_profit = price_pre_tax - price_gold - price_duty - price_stones - price_labor

#     return price_gold, price_stones, price_labor, price_profit, price_duty, price_pre_tax


# custom error class
class CustomErrorBD(Exception):
    pass


# gets profit bases on the itemcode
def random_profit(s, min_value=8.99, max_value=9.16):
    '''
    s: item code
    '''
    hash_value = hash(s.upper())
    normalized_value = float(hash_value)
    scaled_value = min_value + (normalized_value % (max_value - min_value))
    return round(scaled_value,2)


# calculates the total stone price
def get_stones_price(stones_ct, price_stones):
    '''
    Calculates the total price for all the stones
    '''
    price = 0
    for stone in stones_ct.items():
        price += price_stones[stone[0]] * stone[1]
    return round(price)


# increase the stone price
def inc_stones_price(price_stones, condition):
    '''
    price_stones: price per carat for each stone
    condition: tells which stone prices should not be increased
    '''
    abbre = {'Ruby':'rby',
             'Emerald':'emd',
             'Sapphire':'sph',
             'Pearl':'prl',
             'Coral':'crl',
             'Navratna':'nav',
             'Cubic Zirconia':'cz',
             'South Sea Pearls':'ssp',
             'Ruby/Emerald': 're',
             'Other/All stones': 'oth'}
    for stone in price_stones.keys():
        code = abbre[stone]
        if code in condition:
            continue
        if stone in ('Ruby', 'Emerald', 'Ruby/Emerald', 'Sapphire', 
                     'Navratna', 'South Sea Pearls', 'Other/All stones'):
            inc = random.uniform(0.09, 0.11)
        else:
            inc = random.uniform(0.04, 0.06)
        price_stones[stone] = round(price_stones[stone]+inc, 2)
    return price_stones


# checks if stone prices are exceeding
def check_stones_price(price_stones):
    '''
    Returns 'good' if all stones are within their limit
    Returns a list of strings, which contains which stones are over limit
    '''
    res = []
    for stone in price_stones.items():
        if stone[0] == 'Cubic Zirconia' and stone[1] > 9.00:
            res.append('cz')
        if stone[0] == 'Pearl' and stone[1] > 9.00:
            res.append('prl')
        if stone[0] == 'Ruby' and stone[1] > 29.00:
            res.append('rby')
        if stone[0] == 'Emerald' and stone[1] > 29.00:
            res.append('emd')
        if stone[0] == 'Sapphire' and stone[1] > 29.00:
            res.append('sph')
        if stone[0] == 'Navratna' and stone[1] > 29.00:
            res.append('nav')
        if stone[0] == ('South Sea Pearls') and stone[1] > 25.00:
            res.append('ssp')
        if stone[0] == ('Coral') and stone[1] > 15.0:
            res.append('crl')
        if stone[0] == ('Ruby/Emerald') and stone[1] > 29.0:
            res.append('re')
        if stone[0] == ('Other/All stones') and stone[1] > 29.0:
            res.append('oth')
    return [] if len(res) == 0 else res


# initializes the stone prices
def initial_stone_price(stones):
    price_stones = {'Ruby':11.0,
                    'Emerald':11.0,
                    'Sapphire':13,
                    'Pearl':3.0,
                    'Coral':5.0,
                    'Navratna':14.0,
                    'Cubic Zirconia':3.0,
                    'South Sea Pearls':14.0,
                    'Ruby/Emerald': 11.0,
                    'Other/All stones': 11.0}
    init_stones = {}
    for stone in stones.keys():
        init_stones[stone] = price_stones[stone]

    return init_stones


# gets the code for the entered values
def get_codes(stones):
    abbre = {'Ruby':'rby',
             'Emerald':'emd',
             'Sapphire':'sph',
             'Pearl':'prl',
             'Coral':'crl',
             'Navratna':'nav',
             'Cubic Zirconia':'cz',
             'South Sea Pearls':'ssp',
             'Ruby/Emerald': 're',
             'Other/All stones': 'oth'}
    codes = set()
    for stone in stones.keys():
        codes.add(abbre[stone])
    return len(codes)


# hyderabadi breakdown calculations
def hyd_bd(item_code, price, net_wt, gold_22k, stones):

    # the easy part
    price = float(price)
    price_pre_tax = round(price / 1.0825)
    price_duty = round(price_pre_tax * 0.065)
    price_gold = round(net_wt * gold_22k)

    # initial profit
    profit_perc = random_profit(item_code)
    
    # initializing stones value
    price_stones = initial_stone_price(stones)

    # getting codes
    leng = get_codes(stones)

    # finding prices
    while True:
        s_price = get_stones_price(stones, price_stones)
        price_profit = round(profit_perc*price_pre_tax/100)
        rem = price_pre_tax - price_gold - s_price - price_duty - (price_profit*2)
        if rem>0:
            if profit_perc < 10.99:
                profit_perc += 0.01
            condition = check_stones_price(price_stones)
            if len(condition) < leng:
                inc_stones_price(price_stones, condition)
            if profit_perc > 10.99 and len(condition) == leng:
                raise CustomErrorBD("Unable to calculate, exceeds limits")
        else:
            break
    
    remaining = price_pre_tax - price_gold - s_price - price_duty
    temp = round(remaining//2)

    if remaining % 2 == 0:
        price_labor, price_profit = temp, temp
    else:
        price_labor, price_profit = temp+1, temp

    return price_gold, price_stones, s_price, price_labor, price_profit, price_duty, price_pre_tax


# hyderabadi breakdown calculations
def ant_bd(item_code, price, net_wt, gold_22k, stones, polki_flag, polki_ct):

    # the easy part
    price = float(price)
    price_pre_tax = round(price / 1.0825)
    price_duty = round(price_pre_tax * 0.065)
    price_gold = round(net_wt * gold_22k)
    price_polki = 0
    if polki_flag:
        price_polki = round(polki_ct * 295)

    # initial profit
    profit_perc = random_profit(item_code)
    
    # initializing stones value
    price_stones = initial_stone_price(stones)

    # getting codes
    leng = get_codes(stones)

    # finding prices
    while True:
        s_price = get_stones_price(stones, price_stones)
        price_profit = round(profit_perc*price_pre_tax/100)
        rem = price_pre_tax - price_gold - s_price - price_duty - (price_profit*2) - price_polki
        if rem>0:
            if profit_perc < 10.99:
                profit_perc += 0.01
            condition = check_stones_price(price_stones)
            if len(condition) < leng:
                inc_stones_price(price_stones, condition)
            if profit_perc > 10.99 and len(condition) == leng:
                raise CustomErrorBD("Unable to calculate, exceeds limits")
        else:
            break
    
    remaining = price_pre_tax - price_gold - s_price - price_duty - price_polki
    temp = round(remaining//2)

    if remaining % 2 == 0:
        price_labor, price_profit = temp, temp
    else:
        price_labor, price_profit = temp+1, temp

    return price_gold, price_stones, s_price, price_labor, price_profit, price_duty, price_pre_tax, price_polki