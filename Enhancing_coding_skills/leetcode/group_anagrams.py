from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs: list) -> list:
        anagram_map = defaultdict(list)
        result = []

        for element in strs:
            sorted_element = tuple(sorted(element))
            anagram_map[sorted_element].append(element)

        for value in anagram_map.values():
            result.append(value)

        return result

    strings = input()
    groupAnagrams(strings)
