# 设置全局变量
Max =[]
Allocation = []
Need = []
Available = []
num = []
Finish = []
Work = []
LAST_LINE=[]
Adv = 0
m = eval(input("请输入进程数："))
n = eval(input("请输入资源数："))

def Input(List):
    for i in range(0,m):
        num.clear()
        M = list().clear()
        print(f"输入的是进程P{i}")
        for j in range(0,n):
            while True:
                flg = 1
                try:
                    print(f"资源{chr(j+ord('A'))}", end='')
                    B = eval(input(":"))
                except:
                    print("请重新输入：")
                    flag = 0
                if flg==1:
                    num.append(B)
                    M = num.copy()
                    break
        List.append(M)

def Print(Max,Allocation,Need,Available):
    print("\tMax"+"\t"*n+"Allocation"+"\t"*n+"Need")
    for i in range(m):
        for j in range(n):
            print(Max[i][j],end='\t')
        print("\t",end='')
        for j in range(0,n):
            print(Allocation[i][j],end='\t')
        print("\t",end='')
        for j in range(0,n):
            print(Need[i][j],end='\t')
        print("\t")
    print("\n\tAvailable")
    print("\t",end='')
    for i in range(0,n):
        print(Available[i],end="\t")
    print("\n")

def Save(Available,Allocation,Need):
    p=[]
    Work = Available.copy()
    Finish = [0 for i in range(m)]
    i=0
    while i<m:
        if Finish[i]==1:
            i += 1
            continue
        else:
            for j in range(n):
                if Work[j]<Need[i][j]:
                    break
            else:
                Finish[i]=1
                for k in range(n):
                    Work[k] += Allocation[i][k]
                p.append(i)
                i=-1
        i += 1
    if len(p)==m:
        print("系统是安全的，其序列为：")
        for k in range(m):
            print(p[k],end='-->')
        print("结束\t")
        return 1,p
    return 0,p

def Advice(p):
    count = 0
    Adv = p[count]
    for i in range(m):
        if count!=i:
            break
        for j in range(n):
            if Need[Adv][j]!=0:
                break
        else:
            count+=1
            if count==m:
                return -1
            Adv = p[count]
        Adv = p[count]
    return Adv


def main():
    print("请输入Max数组")
    # Input(Max)
    Max=[[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
    # print("***",Max[4][2])
    print("请输入Allocation数组")
    # Input(Allocation)
    Allocation=[[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
    for i in range(m):
        num.clear()
        M = list().clear()
        for j in range(n):
            NB = Max[i][j]-Allocation[i][j]
            num.append(NB)
            M = num.copy()
        Need.append(M)
    while True:
        Available=[]
        for i in range(n):
            while True:
                fi=1
                try:
                    print(f"Available输入的是资源{chr(i+ord('A'))}", end='')
                    NB = eval(input(":"))
                except:
                    print("输入有误！！")
                    fi = 0
                if fi ==1:
                    Available.append(NB)
                    break
        Print(Max,Allocation,Need,Available)
        print('*'*70)
        h,p = Save(Available,Allocation,Need)
        if h==1:
            print("已找到解决路线")
            break
        else:
            print("可能是Available太小了")

    # Print()
# *******************************************************************
    while True:
        Adv = Advice(p)
        if Adv==-1:
            print("你测试的最终路线为：",end='')
            for i in range(m):
                print(LAST_LINE[i],end='-->')
            print("结束")
            print("结束进程分配！")
            break
        print(f"建议你输入的进程为：{Adv}")
        while True:
            f=1
            while True:
                fi=1
                try:
                    mi = eval(input("实际输入需要请求的进程是："))
                except:
                    print("请求的进程输入有误，请重新输入！！")
                    fi=0
                if fi==1:
                    if mi<m:
                        f=0
                    else:
                        print("请求的进程数输入有误!")
                    break
            if f==0:
                break
        while True:
            Request = []
            print("建议你输入的资源数为：",end='')
            for i in range(n):
                print(Need[mi][i],end='\t')
            print("\n")
            for i in range(n):
                while True:
                    fi = 1
                    try:
                        print(f"实际你请求进程{mi}的资源数为{chr(i+ord('A'))}",end='')
                        res = eval(input(":"))
                    except:
                        print("输入错误，请重新输入！！")
                        fi=0
                    if fi==1:
                        Request.append(res)
                        break
            for i in range(n):
                if Request[i]>Need[mi][i] or Request[i]>Available[i]:
                    print("所请求的资源太大！请从新输入")
                    break
            else:
                break
    #             此处有疑问？
        for i in range(n):
            Need[mi][i] -= Request[i]
            Available[i] -= Request[i]
            Allocation[mi][i] += Request[i]
        h,PI=Save(Available,Allocation,Need)
        if h==1:
            print("同意你的请求你的分配！")
            p=PI
            for i in range(n):
                if Need[mi][i]!=0:
                    break
            else:
                for j in range(n):
                    Available[j] = Available[j]+Request[j]+Allocation[mi][j]
                    Allocation[mi][j]=0
                for k in range(n):
                    if Request[k]!=0:
                        LAST_LINE.append(mi)
                        break
            Print(Max,Allocation,Need,Available)
            print('*'*70)
        else:
            print('*'*70)
            print("你的请求被拒绝")

            for i in range(n):
                Need[mi][i] += Request[i]
                Available[i] += Request[i]
                Allocation[mi][i] -= Request[i]
            Print(Max,Allocation,Need,Available)
            print('*' * 70)
            print("请重新输入")

if __name__ == '__main__':
    main()

########################################
########################################
###作者：华攸强##########################
###题目：银行家算法#######################
###完成时间：2019/10/24/01：44###########
########################################
########################################