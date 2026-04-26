"""
5.2PP Collection of Strings
"""

__author__ = "YOUR NAME"


def add_word(word_list: list[str], word: str):
    """
    Adds a new word to the word list if there is capacity and
    the word is not empty.
    """
    word_list = word_list + word
    return word_list
    # TODO: Complete the implementation of this function
    ...


def display_entries(word_list: list[str]):
    """
    Displays all words in the word list, separated by a comma.
    """
    # TODO: Complete the implementation of this function
    ...
def average_len(word_list: list[str]):
    """
    calulate the average length of the words in the list

    
    """
    


def main():
    # TODO: Add necessary variable declarations and initialisations
    # TODO: Implement the menu
    ...
    words: list[str]
    choice: str
    new_word: str 
    print(words)
    while choice != "4":
        print("1. Add a word")
        print("2. Display entries")
        print("3. Display average word length")
        print("4. Quit")
        action = input("Action:")
        if action == 1:
            new_word = input("What word would you like to add?")
            add_word(words, new_word)
        if choice == 2:
            display_entries(words)
        if choice == 3:
            average_len(words)
            
            



if __name__ == "__main__":
    main()
