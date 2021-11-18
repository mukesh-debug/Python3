#!/usr/bin/env python3

def truncate_sentence(sentence, truncation_var):
    """This function will truncate a sentence to specified number of words."""
    words = []
    for index in range(len(sentence)):
        if sentence[index] == ' ':
            words.append(index)

    if truncation_var <= (len(words)):
        return sentence[: words[truncation_var-1]]
    else:
        return sentence

if __name__ == '__main__':

    string = input("Input sentence to be truncated: ")
    truncation_arg = int(input("Input number of words in new sentence: "))
    print()
    print("Truncated sentence: ", truncate_sentence(string, truncation_arg))
