x=[]
test_score=[]
n=int(input())
if __name__ == '__main__':
    for _ in range(n):
        name = input()
        score = float(input())
        test_score.append(score)
        x.append([name, score])

p=set(test_score)
f=list(p)
f.sort()
val=[]
for j in range(n):
    if(x[j][1] == f[1]):
        val.append(x[j][0])

val.sort()
for i in val:
    print(i)
