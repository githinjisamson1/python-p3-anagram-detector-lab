# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    # match()
    def match(self, possibleAnagrams):
        # empty list
        match = []
        
        # word list comprehension
        wordLc = [letter for letter in self.word]
        sortedWordLc = sorted(wordLc)

        for item in possibleAnagrams:
            # item list comprehension
            itemLc = [letter for letter in item]
            sortedItemLc = sorted(itemLc)

            # append to match if matches upon sort
            if sortedWordLc == sortedItemLc:
                match.append(item)

        return match
    
# anagram1=Anagram("listen")
# print(anagram1.match(['enlists', 'google', 'inlets', 'banana']))

