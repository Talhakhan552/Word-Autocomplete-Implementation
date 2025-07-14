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

## File Structure and How to Use

### Files Overview

1. **main.txt**  
   This file contains paths to **book1.txt** and **book2.txt**, which are essential data sources for the Trie. The **main.txt** file points to the text files containing the words to be used for autocomplete.

2. **book1.txt**  
   This text file includes a collection of words that will be loaded into the Trie to provide autocomplete suggestions when users enter a prefix.

3. **book2.txt**  
   Similar to **book1.txt**, this file contains additional words that will be loaded into the Trie for autocomplete functionality.

4. **assignment_4.py**  
   The main Python script where the Trie is implemented. It reads **main.txt**, loads words from **book1.txt** and **book2.txt** into the Trie, and provides autocomplete functionality based on user input.

### How to Use the Files

1. **Ensure the Files Are Accessible**  
   Before running the program, make sure that **main.txt**, **book1.txt**, and **book2.txt** are in the correct directory, or adjust the paths in **main.txt** accordingly to where these files are located on your system.

2. **Run the Program**  
   - Open a terminal and navigate to the directory containing **assignment_4.py**.
   - Run the following command to start the program:
     ```bash
     python assignment_4.py
     ```

3. **Input the File Paths**  
   - The program will ask you to enter the **main.txt** file. This file contains the paths to **book1.txt** and **book2.txt**. Enter the full path to **main.txt** when prompted.

4. **Autocomplete Suggestions**  
   - After the words are loaded from **book1.txt** and **book2.txt**, the program will prompt you to enter a prefix (e.g., "ca").
   - The program will display ranked autocomplete suggestions based on the frequency of the words.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/trie-autocomplete.git
   cd trie-autocomplete

