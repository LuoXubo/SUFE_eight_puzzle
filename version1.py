# coding:utf-8
from matrix_input import load_input
import copy
import operator

class State:
    def __init__(self, m):
        self.node = m
        self.f = 0
        self.g = 0
        self.h = 0
        self.father = None

    def array(self):
        return self.node

def eight_puzzle_step(input_):
    '''
    此函数为同学们需要补全的部分，可以在studentid-name.py文件再写其他函数，在此函数中调用
    例如可以定义：
    def you_code():
        some implement
    :param input_:
    :return:
    '''
    step = 0
    # 请在这里写上你的实现代码
    # you_code()
    result = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]   #最终状态
    direction = [[1,0],[0,1],[-1,0],[0,-1]]      #空格可能移动的方向
    input_ = State(input_)
    input_.g = 0
    input_.h = h(input_)
    input_.f = input_.g+input_.h

    Open = [input_]
    OpenArray = [input_.array()]
    Closed = []
    ClosedArray = []
    flag = False # flag=True: 返回解;  flag=False:  返回-1
    while len(OpenArray):
        # print(step)
        # 找到Open中f值最低的结点
        cmp = operator.attrgetter('f','h')
        Open.sort(key=cmp)
        now = Open[0]
        # print(now.array(), now.f)
        Open.remove(now)
        OpenArray.remove(now.array())
        Closed.append(now)
        ClosedArray.append(now.array())

        if now.array() == result:
            flag = True
            break

        # 找到空格位置
        arr = now.array()
        i0 = 3
        j0 = 3
        for i in range(3):
            for j in range(3):
                if arr[i][j] == 0:
                    i0 = i
                    j0 = j
                    break

        # 遍历空格可能移动的四个方向，并适当剪枝
        for d in range(4):
            temp = copy.deepcopy(now.array())
            r = i0 + direction[d][0]
            c = j0 + direction[d][1]
            if r<0 or r>2 or c<0 or c>2:
                continue
            temp[i0][j0], temp[r][c] = temp[r][c], temp[i0][j0]
            if temp in OpenArray or temp in ClosedArray:
                continue
            temp = State(temp)
            temp.g = step+1
            temp.h = h(temp)
            temp.f = temp.g + temp.h
            Open.append(temp)
            OpenArray.append(temp.array())

        step+=1

    if flag == False:
        step = -1
    return step

# 启发函数 h(n) = 不受阻拦的情况下，n状态移动到最终状态需要的最小步数
def h(a):
    a = a.array()
    res = 0
    idx = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[1,1]]
    for i in range(3):
        for j in range(3):
            num = a[i][j]
            if num == 0:
                res+=abs(i-idx[8][0])+abs(j-idx[8][1])
            else:
                res += abs(i-idx[num-1][0]) + abs(j-idx[num-1][1])
    return res
if __name__ == '__main__':
    input_ = load_input()
    print(eight_puzzle_step(input_))

