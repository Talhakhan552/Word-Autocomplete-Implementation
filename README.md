# Word-Autocomplete-Implementation

This Python program implements a **Trie** (prefix tree) data structure to facilitate **autocomplete** functionality. The trie allows for efficient searching, prefix matching, and word ranking based on frequency of occurrence. This implementation is ideal for applications such as search engines, text editors, and messaging apps that offer real-time word suggestions.

## Features

- **Trie Data Structure**  
  Implements a **Trie** using a dictionary, where each node represents a character. The **wordEnd** flag marks the end of a word, and each word node also stores a **frequency** to track how often a word is used.

- **Autocomplete Functionality**  
  The program allows the user to input a prefix and returns a list of all words starting with that prefix, ranked by their frequency of occurrence.

- **Word Frequency Ranking**  
  Words are ranked based on how frequently they have appeared in the given text files.

- **File Input Handling**  
  The program reads a list of filenames (e.g., `abc.txt`) and processes each file containing words. If a file doesn't exist, it throws an exception.

- **User Interaction**  
  The program prompts the user to input a word prefix, and then returns ranked suggestions. The user can enter a new prefix or exit by entering '0'.

## How It Works

1. **Input Files**  
   The program first asks the user to enter a file name (e.g., `abc.txt`), which contains a list of filenames (e.g., `dictionary.txt`, `novel.txt`). Each file should contain words to be inserted into the Trie.

2. **Trie Node Structure**  
   Each node in the Trie is a dictionary. The `children` field stores the child nodes, the `wordEnd` field indicates if the node marks the end of a word, and the `frequency` field keeps track of how often the word has been inserted.

3. **Autocomplete**  
   The `autoComplete(prefix)` method finds all words starting with the given prefix and ranks them by frequency.

4. **User Input**  
   - The user can input a word prefix (e.g., "ca") to see a ranked list of words starting with that prefix.
   - The program continuously prompts the user until they enter '0' to quit.

5. **Error Handling**  
   - The program checks if the input file exists. If not, it raises an exception.
   - If a file does not exist, it throws an exception and prompts the user for valid files.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/trie-autocomplete.git
   cd trie-autocomplete

