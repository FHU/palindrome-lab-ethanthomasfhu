def palindrome(word):
     word = word.replace(" ", "").lower()
     return word == word[::-1]

def main():
    user_input = input("Enter text: ")
    if palindrome(user_input):
        print("True")
    else:
        print("False")



if __name__ == '__main__': 
    main()
