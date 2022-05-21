
a = input('输入ygo卡组代码：'"\n").replace('&extra',"'#extra").replace("&side","'!side").split("main=")[1]
b = list(a.replace("=","\n"))+["'"]
c = []
v = [-1]

j = 0
for i in range(len(b)):
    if b[i] == "'" or b[i] == "_" :
        j=j+1
        b[i] = "\n"
        v.append(i)
        c.append(b[(int(v[j-1])+1):v[j]])

print("\n""#created by ygopro2")
print("\n""#main")

for x in range(len(c)):
    for y in range(len(c[x])):
        if c[x][y-1] == "*":
            n = c[x][y]
            c[x][y] = "\n"
            c[x].remove(c[x][y-1])
            if n == "2":
                c[x]=c[x]+c[x][:-1]
            elif n =="3":
                c[x]=c[x]+c[x]+c[x][:-1]
    print("".join(c[x]).replace(" ", ""))

s=input('请按任意字符退出：')
