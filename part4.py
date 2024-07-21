def stable_stock_matching(buyers_preferences, stocks_preferences):
    # 맞음
    '''
    my_dict = {}
    for buyer, total_stock in buyers_preferences.items():
        for stock in total_stock:
            print("여기", stock)
            if stock not in my_dict.values():
                my_dict[buyer] = stock
                break
            else:
                pass
    # 여기까지
    '''
    my_dict = {}
    all_stock = [stock_list for stock_lists in buyers_preferences.values() for stock_list in stock_lists]
    stock_set = set(all_stock)
    stocks = list(stock_set)

    for buyer, total_stock in buyers_preferences.items():
        for stock in total_stock:
            # print(buyer, stock, "여기는")
            #print(stock)
            if stock not in my_dict.values():
                my_dict[buyer] = stock
                break
            else:
                pass

    return my_dict


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
