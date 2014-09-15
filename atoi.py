class Solution:
    # @return an integer
    def atoi(self, str):
        return eval(str)

if __name__ == '__main__':
    print Solution().atoi('    +123   ')
