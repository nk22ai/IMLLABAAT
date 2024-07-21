def printtrans(m, k, d, names, owned, prices):
    transactions = []
    
    for i in range(k):
        sname = names[i]
        sowned = owned[i]
        sprices = prices[i]
        n = len(sprices)
        latestsprices = sprices[-1]
        
        avg = sum(sprices[:n-2]) / (n-2)
        
        differ = avg - latestsprices
        
        if differ > 1.5 and m >= latestsprices:
            sharestobuy = int(m // latestsprices)
            if sharestobuy > 0:
                transactions.append(f"{sname} BUY {sharestobuy}")
                m -= sharestobuy * latestsprices
        elif differ < -1.5 and sowned > 0:
            transactions.append(f"{sname} SELL {sowned}")
    
    if transactions:
        print(len(transactions))
        for trans in transactions:
            print(trans)
    else:
        print(0) 

def inputparam():
    m, k, d = map(float, input().split())
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    
    for _ in range(k):
        input2 = input().strip().split()
        names.append(input2[0])
        owned.append(int(input2[1]))
        prices.append(list(map(float, input2[2:])))
        
    return m, k, d, names, owned, prices

m, k, d, names, owned, prices = inputparam()

printtrans(m, k, d, names, owned, prices)
# 90 2 400
# iStreet 10 4.54 5.53 6.56 5.54 7.60
# HR 0 30.54 27.53 24.42 20.11 17.50