#!/usr/bin/python3
"""
a function that prints a text with 2 new lines after each of these characters: ., ? and :

"""
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text into sentences using '.', '?' and ':' as delimiters
    sentences = []
    sentence = ""
    for char in text:
        sentence += char
        if char in ".?:":
            sentences.append(sentence.strip())
            sentence = ""
    if sentence:
        sentences.append(sentence.strip())

    # Print the sentences with 2 new lines after each sentence
    for sentence in sentences:
        print(sentence)
        print()
