class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        i = 0
        while mainTank > 0:
            i += 1
            mainTank -= 1
            distance += 10
            if i%5==0 and additionalTank>0:
                mainTank += 1
                additionalTank -= 1
        return distance