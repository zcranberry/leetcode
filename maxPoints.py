#encoding:UTF-8
#自己运行的结果和leetcode上不一致，Point(0, 0), Point(1, 1), Point(1, -1)
#暂时没有考虑重复点的问题
#可以生成随机数据，和标准的C++答案做比较
import fractions
import collections
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        if len(points) == 1:
            return 1
        slope_map = {}
        slope_map = collections.defaultdict(lambda: 1, slope_map)
        max_count = 0
        for pa in points:
            slope_map.clear()
            count = 0
            for pb in points:
                if pb == pa:
                    continue 
                try:
                    slope_map[fractions.Fraction(pb.y - pa.y, pb.x - pa.x)] += 1
                except:
                    slope_map['vertical'] += 1
            for k, v in slope_map.items():
                max_count = max(max_count, v)
        return max_count

if __name__ == '__main__':
    print Solution().maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)])

                

