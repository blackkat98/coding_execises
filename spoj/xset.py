if __name__ == '__main__':
    t = int(input())
    arr = []
    buckets = {}
    
    while t > 0:
        el = int(input())
        arr.append(el)
        t -= 1
    
    for el in arr:
        buckets[el] = 1
        
    print(len(buckets))
