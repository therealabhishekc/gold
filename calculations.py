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

    return (round(cash * float(gold_wt), 2), 
            round(trade * float(gold_wt), 2), 
            marker)

# print(scrap_gold(80.52, "22K", "10", "Govindji's"))