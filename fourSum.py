import sets
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        length = len(num)
        couple = []
        for i in xrange(0,length):
            for j in xrange(i + 1,length):
                couple.append([i,j])
        sorted_couple = sorted(couple,key = lambda a:num[a[0]] + num[a[1]])

        #print sorted_couple

        len_cp = len(sorted_couple)
        begin, end = 0, len_cp - 1
        result = sets.Set()
        while begin < end:
            quad = [sorted_couple[begin][0],sorted_couple[begin][1],sorted_couple[end][0],sorted_couple[end][1]]
            value = num[quad[0]] + num[quad[1]] +num[quad[2]] + num[quad[3]]
            if value < target:
                begin += 1
            elif value > target:
                end -= 1
            else:
                #both = [val for val in sorted_couple[begin] if val in sorted_couple[end]]
                #if len(both) == 0:
                #if len(sets.Set(sorted_couple[begin]) & sets.Set(sorted_couple[end])) == 0:
                if sorted_couple[begin][0] != sorted_couple[end][0] and sorted_couple[begin][0] != sorted_couple[end][1] and  sorted_couple[begin][1] != sorted_couple[end][0] and sorted_couple[begin][1] != sorted_couple[end][1]:
                    #print quad
                    #print sorted([num[quad[0]],num[quad[1]],num[quad[2]],num[quad[3]]])
                    result.add((tuple(sorted([num[quad[0]],num[quad[1]],num[quad[2]],num[quad[3]]]))))
                begin += 1
                end -= 1
        new_result = []
        for each in result:
        	new_result.append(list(each))
        return new_result


if __name__ == '__main__':
    print Solution().fourSum([1, 0, -1, 0, -2, 2],0)

