#encoding: utf-8
from copy import deepcopy


def isduplicate(li, n, t):
    while n < t:
        if li[n] == li[t]:
            return True
        n += 1
    return False


def swap(li, i, j):
    if i == j:
        return
    temp = li[j]
    li[j] = li[i]
    li[i] = temp


def permutation(li, size, n, result):
    if n == size - 1:
        result.append(deepcopy(li))
        return
    for i in list(range(n, size)):  
        if isduplicate(li, n, i):  
            continue
        swap(li, i, n)  
        permutation(li, size, n + 1, result)  
        swap(li, i, n)  

def getCommandByClient(clientCommand,li):
    result = []
    index = clientCommand.keys()
    countDict = dict(zip(index,[0]*len(index)))
    for i in li:
        count = countDict[i]

        result.append(clientCommand[i][count])
        countDict[i] = countDict[i]+1

    return result

def getCommandList(client):
    li = []
    result = []
    for k,v in client.iteritems():
        li = li+[k]*len(v)
    permutation(li,len(li),0,result)
    return result


if __name__ == '__main__':
    client={'client1':['clent1-command1','clent1-command2'],'clien2':["clent2-command1"]}
    li = []
    for k,v in client.iteritems():
        li = li+[k]*len(v)
    size = len(li)
    n = 0
    result = []
    permutation(li, size, n, result)
    print result

       