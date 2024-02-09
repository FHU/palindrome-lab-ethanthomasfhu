def palindrome(word):
     word = word.replace(" ", "").lower()
     return word == word[::-1]

if __name__ == '__main__': 
    user_input = input("Enter text: ")
    if palindrome(user_input):
        print("True")
    else:
        print("False")


