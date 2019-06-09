if __name__ == '__main__':
    N = int(input())

test= [] #empty list
for i in range(N):
    inp=list(input().split())

    if(inp[0]=='insert'):
        test.insert(int(inp[1]), int(inp[2]))
    elif(inp[0]=='print'):
        print(test)
    elif(inp[0]=='remove'):
        test.remove(int(inp[1]))
    elif(inp[0]=='append'):
        test.append(int(inp[1]))
    elif(inp[0]=='sort'):
        test.sort()
    elif(inp[0]=='pop'):
        test.pop()
    elif(inp[0]=='reverse'):
        test.reverse() 
