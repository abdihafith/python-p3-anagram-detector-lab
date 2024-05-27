# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, possible_anagrams):
        # Normalize the word by sorting its letters
        normalized_word = sorted(self.word)
        
        # Initialize an empty list to hold the matches
        matches = []
        
        # Iterate through the possible anagrams
        for candidate in possible_anagrams:
            # Normalize the candidate by sorting its letters
            normalized_candidate = sorted(candidate)
            
            # Check if the normalized candidate matches the normalized word
            if normalized_candidate == normalized_word:
                matches.append(candidate)
        
        return matches

# Example usage
anagram_checker = Anagram('listen')
possible_anagrams = ['enlists', 'google', 'inlets', 'banana']
print(anagram_checker.match(possible_anagrams))  # Output: ['inlets']

