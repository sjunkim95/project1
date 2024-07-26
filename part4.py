def stable_stock_matching(buyers_preferences, stocks_preferences):

    buyers_list = list(buyers_preferences.keys())
    matched_dict = {}

    while buyers_list:
        buyer = buyers_list.pop(0)
        # To loop the stock preference of the buyer
        for stock in buyers_preferences[buyer]:

            # Check if the stock is already matched
            matched_stock = [items for items in matched_dict.items() if stock in items]

            # If it had not been matched, add to dictionary to match
            if len(matched_stock) == 0:
                matched_dict[buyer] = stock
                break

            # If it had been matched, compare the preference
            elif len(matched_stock) > 0:
                original_buyer = matched_stock[0][0]
                original_stock_buyer_n = stocks_preferences[stock].index(original_buyer)
                potential_stock_buyer_n = stocks_preferences[stock].index(buyer)

                # If statement to compare the preference of the Buyer
                # Check if the stock prefers the new buyer
                if original_stock_buyer_n > potential_stock_buyer_n:
                    # Since stock prefers the new buyer, delete the original_buyer from the dictionary
                    # and, add the original_buyer to the buyer_list to loop again to find the stock match
                    buyers_list.append(original_buyer)
                    del matched_dict[original_buyer]
                    matched_dict[buyer] = stock
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

# Part 5:
# my time space complexity will be O(n)
# because, I have one while loop, based on key of buyers list, and one for loop of dictionary,
# it will be O(m*n)
# since we are calculating the time based on worst case scenario
# The final answer will be O(n^2)

# I have referenced Gale-Shapely Algorithm
"""
https://www.youtube.com/watch?v=Qcv1IqHWAzg&t=453s
https://www.youtube.com/watch?v=o1olHmxDzTw
https://www.youtube.com/watch?v=0m_YW1zVs-Q
https://www.youtube.com/watch?v=FhRf0j068ZA&t=1959s
https://www.youtube.com/watch?v=F4VmhUMgYW4&t=1039s
https://towardsdatascience.com/gale-shapley-algorithm-simply-explained-caa344e643c2
https://littlefoxdiary.tistory.com/21
https://seoneoblog.wordpress.com/2022/08/21/%EA%B2%8C%EC%9D%BC-%EC%84%80%ED%94%8C%EB%A6%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98gale-shapley-algorithm/
https://engineroom.tistory.com/263
https://kcal2845.tistory.com/21
https://velog.io/@gawon1224/Stable-Matching-Algorithm
https://stackoverflow.com/questions/71960289/stable-match-algorithm-for-different-sizes-groups-and-limited-places
https://stackoverflow.com/questions/77856005/stable-marriage-algorithm-variation
https://stackoverflow.com/questions/60361373/gale-shapley-algorithm-stability-test
"""
