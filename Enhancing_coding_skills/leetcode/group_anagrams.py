from collections import defaultdict

strings = input().split(", ")
anagram_map = defaultdict(list)
result = []

for element in strings:
    sorted_element = tuple(sorted(element))
    anagram_map[sorted_element].append(element)

for value in anagram_map.values():
    result.append(value)

print(result)
