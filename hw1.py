def palindrome():
    s = s[::-1]

while True:
    s = input("Введите слово: ")
    print(True if palindrome(s) else False)