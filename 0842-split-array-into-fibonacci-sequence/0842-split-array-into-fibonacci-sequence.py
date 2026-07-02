class Solution:
    def splitIntoFibonacci(self, num):
        res = []

        def backtrack(index):
            if index == len(num) and len(res) >= 3:
                return True

            curr = 0

            for i in range(index, len(num)):
                # leading zero check
                if i > index and num[index] == '0':
                    break

                curr = curr * 10 + int(num[i])

                # 32-bit integer limit
                if curr > 2**31 - 1:
                    break

                size = len(res)

                if size >= 2:
                    s = res[-1] + res[-2]

                    if curr < s:
                        continue
                    elif curr > s:
                        break

                res.append(curr)

                if backtrack(i + 1):
                    return True

                res.pop()

            return False

        backtrack(0)
        return res