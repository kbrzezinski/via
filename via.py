from tran import translations as trans
import random
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import re

#############################################################
# This script:                                              #
# (1) prints a random translation out of the set of 47,     #
# (2) produces a histogram for the word count of all        #
#     translations,                                         #
# (3) produces a list of words which appear only once       #
#     in any of the translations.                           #
#############################################################

# Load the script creating a list of all the translations in
# the dictionary format, e.g. the first record:
#
# {'translation': ['Along the journey of our life half way',
#                  'I found myself again in a dark wood',
#                  'wherein the straight road no longer lay'],
#  'author': 'Dale',
#  'year': '1996'}
from create_df import df

# Choose a random translation from the set of 47 (minus 1,
# as Python lists start from 0)
trans_no = random.randint(1,47)-1


# Print the translation which we chose randomly earlier
print(str(trans_no) + ".")
for line in df[trans_no]['translation']:
   print(line)
print("    (" + df[trans_no]['author'] + ', ' + df[trans_no]['year'] + ")")


# Make a list of all words in the translations
wordsraw = []
for element in df:
   for line in element['translation']:
      word_separated = line.split()
      wordsraw = wordsraw + word_separated


# Remove commas, slashes, dots, semicolons, and colons from
# the list of words. Replace uppercase letters with
# lowercase letters.
words = []
for w in wordsraw:
   w = w.replace(',', '')
   w = w.replace('\'','')
   w = w.replace('.','')
   w = w.replace(';','')
   w = w.replace(':','')
   w = w.lower()
   words.append(w)

   
# Remove empty records from the list.  Next, remove the
# articles "the", "a", "an", and remove words "I" and "of".
words_without_empty_strings = \
   [string for string in words if string != ""]
final = [string for string in words_without_empty_strings \
         if \
         string != "the" and \
         string != "a" and \
         string != "an" and \
         string != "i" and \
         string != "of"]


# Count the words
word_counts = Counter(final)

# Plot a diagram and save it to a png file
fig = plt.figure()
fig_export = pd.Series(final).value_counts().plot(kind='barh',figsize=(7,28),fontsize=13)#.get_figure().savefig('output.png')
fig.tight_layout()
plt.savefig('output.png')


# Make a list of words which appear only once in any of the
# translations
uniq_words = []
for word, count in word_counts.items():
    if count == 1:
        uniq_words.append(word)

uniq_words = sorted(uniq_words)
