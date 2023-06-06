if __name__ == '__main__':
    t = int(input())
    arr = []
    buckets = {}
    
    while t > 0:
        el = int(input())
        arr.append(el)
        t -= 1
    
    for el in arr:
        keylist = buckets.keys()
        
        if el in keylist:
            buckets[el] += 1
        else:
            buckets[el] = 1
            
    maxTimes = 0
    mostFrequentNumbers = []
    
    for key in buckets.keys():
        if buckets[key] > maxTimes:
            maxTimes = buckets[key]
            
    for key in buckets.keys():
        if buckets[key] == maxTimes:
            mostFrequentNumbers.append(key)
        
    print(max(mostFrequentNumbers) if len(mostFrequentNumbers) else 0)
