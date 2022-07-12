class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i][-1] < s[j][-1]:
                    s[i], s[j] = s[j] ,s[i]
        ls  = []
        for i in s:
            ls.append(i[:-1])
        ls =  ' '.join(ls)
   
            
        return ls
        