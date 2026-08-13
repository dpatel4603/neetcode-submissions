class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = ""
        
        for c in s: 
            if c.isalnum():
                cleaned += c.lower()
        
        reversed_cleaned = cleaned[::-1]

        if cleaned == reversed_cleaned:
            return True
        
        else:
            return False
        
    


            
        