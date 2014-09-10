#encoding:UTF-8
import sets 
#def mysorted(fir, sec, thr): #sec <= thr 是本来就保证的 
#    if fir <= sec <= thr:
#       return (fir,sec,thr)
#    elif sec <= fir <= thr:
#        return (sec,fir,thr)
#    else:
#       return (sec,thr,fir)
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSumClosest(self, num, target):
        min_abs = 2 ** 32
        num.sort()
        result = target
        #result = sets.Set()
        #result = []
        length = len(num)
        for i in xrange(0, length):
            if i > 0 and num[i] == num[i -1]:
                pass
            begin, end = 0, length - 1
            while begin < end:
                if i == begin:
                    begin += 1
                    continue
                elif i == end:
                    end -= 1
                    continue
                curr = num[begin] + num[end] + num[i]
                if abs(curr - target) < min_abs:
                    min_abs = abs(curr - target)
                    result = curr
                    #print i,begin,end
                    #print 'sum', curr
                elif curr  == target:
                    return target 
                if curr < target:
                    begin += 1
                elif curr > target:
                    end -= 1
        return result


if __name__ =='__main__':
    import profile
    print Solution().threeSumClosest([0,1,2],1)

