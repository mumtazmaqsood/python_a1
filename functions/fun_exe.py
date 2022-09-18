

# take 3 args and tell which no is greater

def greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c

print(greater(10,20,30))


#define a function that checks either word can read same in backwards

def is_palindrome(name):
    reverse_name = name[::-1]
    if name == reverse_name:
        print(f"{name} is palindrome ")
    else:
        print(f"{name} is not same as {reverse_name}")

is_palindrome("madam")
is_palindrome("mumtaz")












