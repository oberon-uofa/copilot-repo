def main():
    word = input("input: ")
    if len(word) % 2 == 1:
        print(word[len(word) // 2])
    else:
        print(word[len(word) // 2 - 1] + word[len(word) // 2])

main()
