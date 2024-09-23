class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #defining values
        values = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000)
        intS = []

        #initializing intS with the values of its variables
        for a in s:
            intS.append(values[a])
        intS.reverse()

        #these variables will hold iterator and total
        total, a = intS[0], 1
        #using int values we can use conditional statements
        while a < len(intS):
            if intS[a] >= intS[a - 1]:
                total += intS[a]
            else:
                total -= intS[a]
            a += 1

        #returning the value of total
        return total


            
        
