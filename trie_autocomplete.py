# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 02:48:14 2018

@author: YJ
"""

class Trie(object):

    def __init__(self, words):
        self.setup(words)

    def setup(self, words):
        self.trie_dict = {'end_here': False}

        for word in words:
            self.add_word(word)

    def add_word(self, word):

        cur_dict = self.trie_dict

        for char in word:
            if not char in cur_dict:
                cur_dict[char] = {'end_here': False}
            cur_dict = cur_dict[char]

        cur_dict['end_here'] = True

    def check_for(self, word):
            `
        index = 0
        cur_dict = self.trie_dict

        while word[index] in cur_dict:
            if index + 1 == len(word):
                return cur_dict[word[index]]['end_here']
            
            cur_dict = cur_dict[word[index]]
            index += 1

        return False

    def get_all_with_prefix(self, prefix):
        node = self.get_node_from_prefix(prefix)
        return [prefix + word for word in self.recursive_collect(node)]

    def recursive_collect(self, node, char_prefix=''):
        
        words = []
        if node.get('end_here'):
            words.append(char_prefix)

        for char in node:
            if char == 'end_here':
                continue

            temp_words = [char_prefix + word for word in
                          self.recursive_collect(node[char], char_prefix=char)]
            
            words.extend(temp_words)

        return words

    def get_node_from_prefix(self, prefix):
        cur_dict = self.trie_dict
        index = 0

        while prefix[index] in cur_dict:
            if index + 1 == len(prefix):
                return cur_dict[prefix[index]]

            cur_dict = cur_dict[prefix[index]]
            index += 1

        return {'end_here': False}

my_trie = Trie(['man', 'manm', 'mat', 'china', 'chinese', 'chit'])
assert my_trie.check_for('man')
assert my_trie.check_for('manm')
assert my_trie.check_for('china')
assert not my_trie.check_for('manbm')
assert not my_trie.check_for('ma')

print(my_trie.get_all_with_prefix('ma'))
print(my_trie.get_all_with_prefix('chin'))