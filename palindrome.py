"ana"
"facundo"

def is_palindrome(word: str) -> bool:
    word = word.replace(" ", "").lower()
    return word == word[::-1]

    # "Ana" == "anA"
    
def main():
    print(is_palindrome("ana"))
    print(is_palindrome("facundo"))
    print(is_palindrome(1000))
    
if __name__ == "__main__":
    main()