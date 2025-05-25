def check_delimiters(sequence):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in sequence:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            stack.pop()
    
    return "Симетрично" if not stack else "Несиметрично"

# Приклади
print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(check_delimiters("( 23 ( 2 - 3);"))             # Несиметрично
print(check_delimiters("( 11 }"))                     # Несиметрично