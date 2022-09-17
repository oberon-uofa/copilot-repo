def main():
    char = input("input: ")[0].lower()
    if char in ('a', 'e', 'i', 'o', 'u'):
        print("vowel")
    elif char.isalpha():
        print("consonant")
    else:
        print("neither haha")

if __name__ == "__main__":
    main()
    
