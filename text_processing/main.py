import random


data = 'ala ma kota i lubi jeść parówki'

shuffle_list = []


split_data = data.split()
for word in split_data:
    if len(word) > 1:
        new_word = ''
        new_word += word[0]
        random_sample = random.sample(word[1:-1], len(word[1:-1]))

        for char_random_sample in random_sample:
            new_word += char_random_sample
        new_word += word[-1]
        shuffle_list.append(new_word)
    else:
        shuffle_list.append(word)

