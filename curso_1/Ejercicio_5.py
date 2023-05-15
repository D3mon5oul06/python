#ejercicio 0:
a = ""
length = 0
q0.a.check()

#ejercicio 0b:
b = "it's ok"
length = 7
q0.b.check()

#ejercicio 0c:
c = 'it\'s ok'
length = 7
q0.c.check()

#ejercicio 0d:
d = """hey"""
length = 3
q0.d.check()

#ejercicio 0e:
e = '\n'
length = 1
q0.e.check()

#ejercicio 1:
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()
    pass

# Check your answer
q1.check()

#ejercicio 2:
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    matches = []
    for i, document in enumerate(doc_list):
        document_lower = document.lower()
        keyword_lower = keyword.lower()

        words = document_lower.split()

        cleaned_words = [word.strip(".,") for word in words]

        if keyword_lower in cleaned_words:
            matches.append(i)
    
    return matches
    pass

#ejercicio 3:
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    search_results = {}
    for keyword in keywords:
        search_results[keyword] = word_search(doc_list, keyword)

    return search_results
    pass

