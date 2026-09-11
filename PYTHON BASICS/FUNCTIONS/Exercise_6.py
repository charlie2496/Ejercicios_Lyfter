def sort_words(text):
    words_list = text.split("-")
    words_list.sort()
    sorted_text = "-".join(words_list)
    return sorted_text
input=input("Enter words separated by a hyphen: ")
print(sort_words(input))