import collections
user_string = input("Enter a str:")
letter_list = list(user_string)
dictionary = {}
dictionary = collections.Counter(letter_list)
for k,v in dictionary.items():
    print(k,v)