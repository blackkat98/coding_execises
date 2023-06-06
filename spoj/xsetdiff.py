if __name__ == '__main__':
    n, m = input().split(' ')
    n, m = int(n), int(m)
    N = input().split(' ')
    M = input().split(' ')
    
    for i in range(len(N)):
        N[i] = int(N[i])
        
    for i in range(len(M)):
        M[i] = int(M[i])
    
    maxN = max(N)
    maxM = max(M)
    max = maxM if maxM > maxN else maxN
    
    buckets = []
    
    for i in range(int(max) + 1):
        buckets.append(0)
        
    for num in N:
        if buckets[num] < 1:
            buckets[num] += 1
        
    for num in M:
        if buckets[num] == 1:
            buckets[num] += 1
        
    res = []
    
    for i in range(len(buckets)):
        if buckets[i] == 2:
            res.append(i)
            
    print(' '.join(map(str, res)))
    