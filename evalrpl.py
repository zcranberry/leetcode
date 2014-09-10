class Solution:
    def evalRPN(self,tokens):
            length = len(tokens)
            stk = []
            for i in range(0, length):
                if tokens[i].isdigit() or (tokens[i][0] == '-' and len(tokens[i]) > 1):
                    stk.append(tokens[i])
                else:
                    op2 = stk.pop()
                    op1 = stk.pop()
                    if tokens[i] == '/':
                        res = eval(op1 + '/' + op2)
                        left = eval(op1 + '%' + op2)
                        if res < 0 and left != 0:
                            res += 1
                        stk.append(str(res))
                    else:
                        stk.append(str(eval('(' + op1 + ')' +tokens[i] + '(' +op2 + ')')))
                #print stk
            print(eval(stk[0]))
            return eval(stk[0])

    def __init__(self,tokens):
        self.tokens = tokens

if __name__ == "__main__":
    slu = Solution(["4","-2","/","2","-3","-","-"])
    slu.evalRPN(slu.tokens)

