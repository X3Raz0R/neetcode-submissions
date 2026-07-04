class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        resultat = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and t > temperatures[stack[-1]]:
                pop_i = stack.pop()
                resultat[pop_i] = i - pop_i
            stack.append(i)
        return resultat
