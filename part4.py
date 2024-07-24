def stable_stock_matching(buyers_preferences, stocks_preferences):
    buyers_list = list(buyers_preferences.keys())
    matched_dict = {}
   # print(buyers_list)

    while buyers_list:
        buyer = buyers_list.pop(0)
       # print("Current Buyer is :", buyer)
        for stock in buyers_preferences[buyer]:
         #   print("Current Stock is: ", stock)
          #  print("matched_dict before matched_stock", matched_dict)
            matched_stock = [items for items in matched_dict.items() if stock in items]
           # print("matched_stock: ", matched_stock)

            if len(matched_stock) == 0:
                matched_dict[buyer] = stock
             #   print("현재 buyer list는:", buyers_list)
              #  print("업데이트 직후 match_dict:", matched_dict)
                break

            elif len(matched_stock) > 0:
               # print("현재 len > 1 파트임")
                current_buyer = matched_stock[0][0]
                current_stock = stocks_preferences[stock].index(current_buyer)
                potential_stock = stocks_preferences[stock].index(buyer)
                #print("current_stock:", current_stock)
               # print("potential_stock:", potential_stock)
                if current_stock > potential_stock: # I should pair this stock to a new buyer
                     #   print(f"match is full {current_buyer}")
                   # else:
                   # print(f"{buyer} is picked than {current_buyer}")
                    buyers_list.append(current_buyer)
                     # this stock is matched to new buyer -> buyer = buyers_list.pop(0)
                    # and current  is available again -> current_buyer = matched_stock[0][0]
                    del matched_dict[buyer]
                    break

    return matched_dict

buyers_preferences = {
    'Buyer1': ['StockA', 'StockB', 'StockC'],
    'Buyer2': ['StockB', 'StockA', 'StockC'],
    'Buyer3': ['StockA', 'StockB', 'StockC']
}
stocks_preferences = {
    'StockA': ['Buyer1', 'Buyer2', 'Buyer3'],
    'StockB': ['Buyer2', 'Buyer1', 'Buyer3'],
    'StockC': ['Buyer1', 'Buyer2', 'Buyer3']
}

print(stable_stock_matching(buyers_preferences, stocks_preferences))

