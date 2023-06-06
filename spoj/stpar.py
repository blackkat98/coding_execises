def arrIsSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
        
    return True

def paradeIsPossible(arr):
    parade = []
    queue = []
    
    for i in range(len(arr)):
        if i < len(arr) - 1:
            if arr[i] > arr[i + 1]:
                queue.append(arr[i])
            else:
                parade.append(arr[i])
        else:
            parade.append(arr[i])
            
        while len(queue) and len(parade) and int(parade[len(parade) - 1]) + 1 == int(queue[len(queue) - 1]):
            parade.append(queue[len(queue) - 1])
            del queue[len(queue) - 1]
            
    return arrIsSorted(parade)

if __name__ == '__main__':
    while (True):
        num = int(input())
        arr = input().split(' ')
        endOfInput = input()
        
        if endOfInput != '0' or num != len(arr):
            continue
        
        print('yes' if paradeIsPossible(arr) else 'no')
