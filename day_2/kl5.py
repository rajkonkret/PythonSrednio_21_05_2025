# longest() - znajduje najdłuższy klucz w słowniku
class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


dictionary = LongestKeyDict()
print(dictionary.longest_key())  # None

dictionary['tomasz'] = 9
dictionary['abraham'] = 45
dictionary['zen'] = 42

print(dictionary.longest_key())  # abraham - najdłuższy klucz
