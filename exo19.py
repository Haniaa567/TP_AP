myset=set()
while True:
    word=input("Enter a word: ")
    if word in myset:
        print(myset)
        print("you typed in two unique word")
        exit()
    else:
        myset.add(word)
        print(myset)