class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        masini = {}

        for p, s in zip(position, speed):
            masini[p] = s

        masini = dict(sorted(masini.items(), reverse=True))

        for p, s in masini.items():
            timp = (target - p) / s

            if not stack or timp > stack[-1]:
                stack.append(timp)

        return len(stack)