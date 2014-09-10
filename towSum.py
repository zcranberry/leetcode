class Solution:
    # @return a tuple, (index1, index2)
    def __init__(self,num,target):
        self.num = num
        self.target = target
    def twoSum(self, num, target):
        
        num_list= []
        count = 1
        for i in num:
            num_list.append([i,count])
            count += 1

        def sec(v):
            return v[0]
        num_list.sort(key = sec)

        [i,j] = [0, len(num) - 1]
        while num_list[i][0] + num_list[j][0] != target:
            if num_list[i][0] + num_list[j][0] < target:
                i += 1
            else: 
                j -= 1
        return tuple(sorted([num_list[i][1],num_list[j][1]]))
if __name__ == '__main__':
    slu = Solution([3,2,4], 6)
    print slu.twoSum(slu.num,slu.target)
    slu = Solution([150,24,79,50,88,345,3], 200)
    print slu.twoSum(slu.num,slu.target)

