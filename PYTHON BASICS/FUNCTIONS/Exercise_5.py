def count_letters(text):
    upper_count=0
    lower_count=0
    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
text=input("Enter words: ")
upper, lower = count_letters(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)