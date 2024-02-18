def count_words(text):
    """
    Function to count the number of words in the given text.
    """
    # Split the text into words using whitespace as delimiter
    words = text.split()
    # Return the number of words
    return len(words)


def main():
    """
    Main function to prompt user for input, count words, and display the result.
    """
    print("Welcome to the Word Count Program!")

    # Prompt user for input
    text = input("Please enter a sentence or paragraph: ").strip()

    # Check for empty input
    if not text:
        print("Error: Input is empty. Please provide some text.")
        return

    # Count the words
    word_count = count_words(text)

    # Display the word count
    print(f"\nWord count: {word_count}")


# Call the main function to execute the program
if __name__ == "__main__":
    main()
