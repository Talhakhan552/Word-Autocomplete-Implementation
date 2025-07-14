###########################################

# Talhakhan552 (GITHUB)
# (TRIE)

##########################################

import time


class TrieNode:
    def __init__(self):
        self.child = {}
        self.wordend = False
        self.frequency = 1


class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        temp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if index not in temp.child:
                temp.child[index] = TrieNode()
            temp = temp.child[index]
        temp.wordend  = True
        temp.frequency +=1
        
    
    def search(self,word):
        temp = self.root
        for char in word:
            index = ord(char) - ord('a')
            if index not in temp.child:
                return None
            temp = temp.child[index]
        
        return temp
    

    def collect_word(self, node , prefix, words):
        if node.wordend:
            words.append((prefix, node.frequency))
        for index,child in node.child.items():
            new_prefix = chr(index + ord("a"))
            
            self.collect_word(child,prefix + new_prefix,words)
            
            
    def start_word(self,prefix):
        node = self.search(prefix)
        if node is None:
            return []
        
        words = []
        self.collect_word(node,prefix,words)
        words.sort(key=self.get_frequency, reverse=True)#reverse ke decending me ho 
        return words
    
    def get_frequency(self, ttuple):
        return ttuple[1]



def load_file(file_name):
    trie = Trie()
    total_words = 0
    
    start_time = time.time()
    
    try:
        with open(file_name, 'r',encoding="utf-8") as file_list:
            #file_list 
            for listed_file in file_list:
                listed_file = listed_file.strip()
                if listed_file:
                    try:
                        with open(listed_file , 'r' ,encoding="utf-8") as word_file:
                            #word_file
                            wordz = word_file.read().split()
                            if len(wordz) == 0:
                                print(f"File {listed_file} is empty :(")
                                
                            for word in wordz:
                                clear_word = ''
                                for ch in word:
                                    if 'a'<= ch.lower() <= 'z':
                                        clear_word += ch.lower()
                                if len(clear_word) > 0:
                                    trie.insert(clear_word)
                                    total_words+= 1
                                    
                    except FileNotFoundError:
                        print(f"Error!! cannot find file {listed_file} ")
                        
                        
    except FileNotFoundError:
        print(f"Error!! cannot find file {file_name} ")
        
    endtime = time.time()
    
    comp_time = (endtime - start_time)
    print(f"{file_name} loaded {total_words} words loaded into trie in {comp_time:0.1f} seconds") 
    
    if total_words==0:
        return None
    
    
    return trie
                

def runner_program():
    filename = input("Enter file to load==> ")
    trie = load_file(filename)
    if not trie:
        print("Words not loaded from file :(")
        return


    while True:
        prefix = input("Enter prefix (Enter 0 TO QUIT)==> ")
        if prefix == '0':
            print("Goodbye!!! ")
            break
        results = trie.start_word(prefix.lower())
        if not results:
            print("suggestions not found :( ")
        else:
            print(f"Ranked Suggestions for {prefix}: ")
            for word,freq in results:
                print(f"-> {word} (frequency: {freq})")
            print("="*27)


(runner_program())

































