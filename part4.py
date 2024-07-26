def stable_stock_matching(buyers_preferences, stocks_preferences):

    buyers_list = list(buyers_preferences.keys())
   # print(buyers_list)

    matched_dict = {}
    while buyers_list:
        buyer = buyers_list.pop(0)
     #   print("현재 Buyer는: ", buyer)
        check = list(matched_dict.keys())
        for new_stock in buyers_preferences[buyer]:
            if new_stock not in matched_dict.values():
               # print("뉴스탁과 바이어", new_stock, buyer)
                matched_dict[buyer] = new_stock
               # print("matched_dict", matched_dict)
                break
            else:
               # print("else문")
                if len(check) > 0:
                    for original_buyer in check:
                     #   print(original_buyer,"의기존 바이어의 스탁", matched_dict[original_buyer])
                        if new_stock == matched_dict[original_buyer]:
                            new_stock_pref = stocks_preferences[new_stock].index(buyer)
                            original_stock_pref = stocks_preferences[new_stock].index(original_buyer)
                         #   print("현재 바이어 넘버", new_stock_pref)
                         #   print("기존 바이어 넘버", original_stock_pref)
                            if original_stock_pref > new_stock_pref:
                              #  print("들어옴")
                                del matched_dict[original_buyer]
                                matched_dict[buyer] = new_stock
                              #  print(matched_dict)
                                buyers_list.append(original_buyer)
                                check.clear()
                                break
                else:
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
# because, I have one while loop, based on key of buyers list, one for loop of dictionary, and one loop of list,
# it will be O(m*n*n)
# since we are calculating the time based on worst case scenario
# The final answer will be O(n^3)

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
