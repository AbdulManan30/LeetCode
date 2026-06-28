'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"
'''

def reverseVowels(s):
    vowels = ["a","e","i","o","u", "A","E","I","O","U"]
    detectedVowels = []
    for char in s:
        if char in vowels:
            detectedVowels.append(char)
    detectedVowels.reverse()
    i = 0
    j = 0
    result = ""
    while i<len(s):
        if s[i] in vowels:
            result += detectedVowels[j]
            j += 1
        else:
             result += s[i]
        i+=1
    return result