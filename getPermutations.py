#encoding:UTF-8
import sets
import itertools
def fact(n):
    return n * fact(n-1) if n > 1 else 1
class Solution:
    # @return a string
    #用算数的方法直接算出对应序号的排列
    def getPermutation(self, n, k):# requires 0 < n <= 9
        num = []
        k = k - 1
        num_pool = range(1, n + 1)
        divisor = fact(n - 1)
        for i in range(n - 1, 0, -1):
            quotient = k / divisor
            k = k % divisor
            divisor /= i 
            num.append(num_pool[quotient])
            del num_pool[quotient]
        num.append(num_pool[0])
        return num
    
    #获得所有permutations
    def permute(self,num):
        result = []
        for i in xrange(0, fact(num)):
            result.append(self.getPermutation(num, i + 1))
        return result

    #获取次大的排列，如123->132
    def nextPermutation(self, num):
        found = False
        n = len(num)
        for i in xrange(n - 1, 0, -1):
            if num[i] > num[i - 1]:
                small = num[i - 1]
                for j in xrange(n -1, i - 1, -1):
                    if num[j] > small:
                        num[i - 1], num[j] = num[j], num[i - 1]
                        found = True
                        break
                break
                #找到一个正序的地方，把大的数放在前面，小的数和后面的一起做一个升序

        if found == False:
        	return sorted(num)
        res = num[:i]
        sorted_num = sorted(num[i:])
        for number in sorted_num:
            res.append(number)
        return res

    def permute(self,num):#自带的函数
        perm = itertools.permutations(num)
        return list(perm) 

    def permuteUnique(self,num):
        result = sets.Set()
        perm = itertools.permutations(num)
        for w in perm:
        	result.add(w)
        res = []
        for w in result:
        	res.append(list(w))
        return res




if __name__ == '__main__':
    #print Solution().getPermutation_slow(9,13531)
    #print Solution().nextPermutation([3,2,1])
    print Solution().permuteUnique([1,2,2])


        

