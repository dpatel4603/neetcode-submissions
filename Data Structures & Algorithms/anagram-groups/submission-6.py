class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        anagram_map = defaultdict(list)

        for word in strs: 

            word_sorted = tuple(sorted(word))

            anagram_map[word_sorted].append(word)


        
        return list(anagram_map.values())


    