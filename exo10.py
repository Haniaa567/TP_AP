word=str(input("enter the word: "))
test=True
for i,c in enumerate(word):
    if c!=word[len(word)-1-i]:
        test=False
        break
        
if test:
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.") 