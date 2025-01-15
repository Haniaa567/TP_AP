def anagrams(str1,str2):
    return sorted(str1) == sorted(str2)
print(anagrams("tame", "meta"))
print(anagrams("tame", "mate"))
print(anagrams("tame", "team")) 
print(anagrams("tabby", "batty")) # False 
print(anagrams("python", "java")) # False