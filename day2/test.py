print("aaa")

food=['치킨','토마토','냉면']
print(food[0])
food[1]="초밥"
print(food[1])

coin = {
    'BTC': {
        'opening_price': '44405000',
        'closing_price': '38806000',
        'min_price': '36640000',
        'max_price': '44999000',
        'prev_closing_price': '44404000',
        'fluctate_24H': '-7463000',
        'fluctate_rate_24H': '-16.13',
    },
    'ETH': {
        'opening_price': '1458000',
        'closing_price': '1229000',
        'min_price': '1100000',
        'max_price': '1490000',
        'prev_closing_price': '1458000',
        'fluctate_24H': '-275000',
        'fluctate_rate_24H': '-18.28',
    },
    'XRP': {
        'opening_price': '364.5',
        'closing_price': '311.9',
        'min_price': '284.2',
        'max_price': '372.7',
        'prev_closing_price': '364.2',
        'fluctate_24H': '-90.6',
        'fluctate_rate_24H': '-22.51',
    },
}
btc = coin.get('BTC')
btc_max = btc.get('max_price')
print(btc_max)

btc_open = btc.get('opening_price')
xrp = coin.get('XRP')
xrp_open = xrp.get('opening_price')
print(int(btc_open) + float(xrp_open) )



# 1.코인의 정보에서 BTC의 최대가격을 출력하세요.
print(coin['BTC']['max_price'])
# 2. BTC의 시가와 (opening price) XRP의 시가를 더한 결과를 출력하시오.
result = int(coin['BTC']['opening_price']) + float(coin['XRP']['opening_price'])
print(result, type(result))


movie = {
    'movieInfo': {
        'movieNm': '광해, 왕이 된 남자',
        'movieNmEn': 'Masquerade',
        'showTm': '131',
        'prdtYear': '2012',
        'openDt': '20120913',
        'typeNm': '장편',
        'nations': [{'nationNm': '한국'}],
        'genres': [{'genreNm': '사극'}, {'genreNm': '드라마'}],
        'directors': [{'peopleNm': '추창민', 'peopleNmEn': 'CHOO Chang-min'}],
        'actors': [
            {'peopleNm': '이병헌', 'peopleNmEn': 'LEE Byung-hun', 'cast': '광해/하선'},
            {'peopleNm': '류승룡', 'peopleNmEn': 'RYU Seung-ryong', 'cast': '허균'},
            {'peopleNm': '한효주', 'peopleNmEn': 'HAN Hyo-joo', 'cast': '중전'},
        ],
    }
}

print(movie['movieInfo']['movieNm'])
print(movie['movieInfo']['directors'][0]['peopleNmEn'])
print(len(movie['movieInfo']['actors']))