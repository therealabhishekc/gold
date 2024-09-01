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