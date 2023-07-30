class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def is_self_dividing(num: int):
            for i in str(num):
                if i == '0':
                    return False
                if num % int(i) != 0:
                    return False
            return True
        
        result = []
        for i in range(left, right+1):
            if is_self_dividing(i):
                result.append(i)
        return result