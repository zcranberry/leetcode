import sets 
def mysorted(fir, sec, thr):
    if fir <= sec <= thr:
    	return (fir,sec,thr)
    elif sec <= fir <= thr:
        return (sec,fir,thr)
    else:
    	return (sec,thr,fir)
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        num.sort()
        result = sets.Set()
        #result = []
        length = len(num)
        for i in xrange(0, length):
            if i > 0 and num[i] == num[i -1]:
                continue
            begin, end = 0, length -1
            target = - num[i]
            while begin < end:
                if i == begin:
                    begin += 1
                elif i == end:
                    end -= 1
                elif num[end] + num[begin] == target:
                    result.add(mysorted(num[i], num[begin], num[end]))
                    #result.append(mysorted(num[i], num[begin], num[end]))
                    begin += 1
                    end -= 1
                elif num[end] + num[begin] < target:
                    begin += 1
                else:
                    end -= 1
        return list(result)

def foo():
    print Solution().threeSum(([-7,2,1,10,9,-10,-5,4,13,-9,-4,6,11,-12,-6,-9,-6,-9,-11,-4,10,10,-3,-1,-4,-7,-12,-15,11,5,14,11,-7,-8,6,9,-2,9,-10,-12,-15,2,10,4,5,11,10,6,-13,6,-13,12,-7,-9,-12,4,-9,13,-4,10,4,-12,6,4,-5,-10,-2,0,14,4,4,6,13,-9,-5,-5,-13,12,-14,11,3,10,8,11,-13,4,-8,-7,2,4,10,13,7,2,2,9,-1,8,-5,-10,-3,6,3,-5,12,6,-3,6,3,-2,2,14,-7,-13,10,-13,-2,-12,-4,8,-1,13,6,-9,0,-14,-15,6,9]))

if __name__ =='__main__':
    import profile
    profile.run("foo()")
    print Solution().threeSum([])


        
