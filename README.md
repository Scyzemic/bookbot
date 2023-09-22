# bookbot

This toy program analyzes a text file and provides information about the word count and character count. The program includes two functions: `count_words` and `char_count`.

## Installation

To use this program, you will need to have Python 3 installed on your computer. You can download Python from the official website: [python downloads](https://www.python.org/downloads/)

## Usage

To use the program, run the `main.py` file and provide the path to the text file you want to analyze. For example:

```sh
python main.py books/frankenstein.txt
```

The program will output the word count and character count for the specified file.

## Functions

### `count_words(file_contents)`

This function takes a string as input, splits it into words, counts the number of words, and prints the result.

### `char_count(file_contents)`

This function takes a string as input, creates a dictionary of character counts (case-insensitive), sorts the dictionary by character, and prints the count for each alphabetical character.

## License

This program is licensed under the MIT License. See the `LICENSE` file for more information.
