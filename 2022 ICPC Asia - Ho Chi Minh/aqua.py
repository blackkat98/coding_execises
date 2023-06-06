def isValidTopString(str):
    for charIndex in range(0, len(str) - 1):
        if charIndex % 2 and str[charIndex] != '_':
            return False
        
        if not charIndex % 2 and str[charIndex] != ' ':
            return False
        
    return True

def isValidBottomString(str):
    if str[0] != '|' or str[len(str) - 1] != '|':
        return False
    
    for charIndex in range(0, len(str) - 1):
        if charIndex % 2 and str[charIndex] != '_':
            return False
        
    return True

def isValidString(str):
    if str[0] != '|' or str[len(str) - 1] != '|':
        print(1)
        return False
    
    for charIndex in range(0, len(str) - 1):
        if charIndex % 2 and (str[charIndex] != '_' and str[charIndex] != ' '):
            print(2)
            return False
        
        if not charIndex % 2 and (str[charIndex] != '|' and str[charIndex] != ' '):
            print(3)
            return False
        
    return True

def main(row, col, board, requirements):
    
    
    return

row, col = input().split(' ')
row, col = int(row), int(col)
rowCounter = 0
board = []

while rowCounter <= row:
    lineInput = input()
    
    if rowCounter == 0 and not isValidTopString(lineInput):
        raise Exception('Invalid top')
    
    if rowCounter == row and not isValidBottomString(lineInput):
        raise Exception('Invalid bottom')
    
    if len(lineInput) != (2 * col + 1):
        raise Exception('Invalid number of elements in a row')
    
    if not rowCounter == 0 and not isValidString(lineInput):
        raise Exception('Invalid row')
    
    board.append(lineInput)
    rowCounter += 1
    
requirements = input().split(' ')

if len(requirements) != row:
    raise Exception('Invalid number of requirements')

for i in range(len(requirements) - 1):
    requirements[i] = int(requirements[i])
    
print(main(row, col, board, requirements))
