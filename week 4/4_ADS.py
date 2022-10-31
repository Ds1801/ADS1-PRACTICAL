
import pandas as pd
import clean_up as cl

text = open("big_data.txt", 'r')

with open("big_data.txt", 'r') as text:
    all_words = []
    counter = 0
    for line in text:
        words = line.split()
        counter = counter + 1

        for word in words:
            word = cl.clean(word)
            all_words.append(word)

def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print("Number of Words: ", counter)        
print(len(all_words))
print("Longest word is: ", longest_word('big_data.txt'))

df_words = pd.DataFrame(data = all_words, columns = ("words",))
df_counts = df_words["words"].value_counts()
print(df_counts)
