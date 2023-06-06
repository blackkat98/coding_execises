def getOpenBracketChar(closeBracketChar):
    if closeBracketChar == ')':
        return '('
    
    if closeBracketChar == ']':
        return '['
    
    if closeBracketChar == '}':
        return '{'

def isBlanced(expression):
    bucket = []
    
    for index in range(len(expression)):
        char = expression[index]
        
        if char in [ '(', '[', '{' ]:
            bucket.append(char)
        else:
            matchingOpenBracket = getOpenBracketChar(char)
            
            if not len(bucket):
                return False
            else:
                if bucket[len(bucket) - 1] != matchingOpenBracket:
                    return False
                else:
                    del bucket[len(bucket) - 1]
                        
    return not len(bucket)

if __name__ == '__main__':
    n = int(input())
    expressions = []
    
    while n > 0:
        item = input()
        expressions.append(item)
        n -= 1
        
    for expression in expressions:
        if isBlanced(expression):
            print('YES')
        else:
            print('NO')
    