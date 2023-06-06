def charIsOperator(char):
    return char in [ '+', '-', '*', '/', ':', '^' ]

def getOperatorLevel(operator):
    if operator == '+' or operator == '-':
        return 1
    
    if operator == '*' or operator == '/' or operator == ':':
        return 2
    
    if operator == '^':
        return 3
    
    return 0

def charIsOperand(char):
    return (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z')

def transform(expression):
    res = ''
    stack = ''
    
    for i in range(len(expression)):
        char = expression[i]
        
        if charIsOperand(char):
            res += char
            
        if char == '(':
            stack += char
            
        if char == ')':
            for j in reversed(range(len(stack))):
                top = stack[j]
                
                if charIsOperator(top):
                    res += top
                    stack = stack[:-1]
                    
                if top == '(':
                    stack = stack[:-1]
                    break
                
        if charIsOperator(char):
            for j in reversed(range(len(stack))):
                top = stack[j]
                
                if not charIsOperator(top):
                    break
                else:
                    if getOperatorLevel(top) >= getOperatorLevel(char):
                        res += top
                        stack = stack[:-1]
                        
            stack += char
            
    for i in reversed(range(len(stack))):
        res += stack[i]
        stack = stack[:-1]
        
    return res
   
if __name__ == '__main__':
    t = int(input())
    expressions = []
    
    while t > 0:
        item = input()
        expressions.append(item)
        t -= 1
        
    for expression in expressions:
        print(transform(expression))
