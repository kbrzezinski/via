# Import the file containing the translations
from tran import translations


# Initiate the frame for storing info about poems
df = []
# Initiate the iterator for a loop
poem_no = 1
# Starting position of the first poem in translations
start_of_poem = 0


while poem_no < 48:
    # For every poem except the last one, find end of poem
    # by finding the start of the next poem.  Next, extract
    # every poem and its author and year.  Every poem is
    # stored as a set of lines.
    
    if poem_no < 47:
        end_of_poem = translations.find(str(poem_no+1) + '.')
    else:
        # End of the last poem is the end of the string
        end_of_poem = len(translations)
        
    contents = translations[start_of_poem:end_of_poem]
    remove_no = contents.partition("\n")[2]
    poem, author_and_year = remove_no.split("\n    (")
    author = author_and_year[:-8]
    year = author_and_year[-6:-2]
    lines = poem.split("\n")
    
    this_poem = {
        'translation': lines,
        'author': author,
        'year': year,
        #'lines': lines
    }
    
    df.append(this_poem)
    poem_no += 1
    start_of_poem = end_of_poem

