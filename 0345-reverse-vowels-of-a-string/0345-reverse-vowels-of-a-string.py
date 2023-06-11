class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        s_list = [char for char in s]
        i = 0
        j = len(s_list) - 1
        
        while i < j:
            if s_list[i] in vowels and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                
                i += 1
                j -= 1
                
            elif s_list[i] in vowels:
                j -= 1
                
            elif s_list[j] in vowels:
                i += 1
                
            else:
                i += 1
                j -= 1
                
        return "".join(char for char in s_list)