def pali(s):
    s = s.lower().replace(" ", "") 
    return s == s[::-1] 
text = input("Enter a string: ")
if pali(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
