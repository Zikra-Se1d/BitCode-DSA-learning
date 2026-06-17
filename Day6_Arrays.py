if __name__ == '__main__':
    N = int(input())
    
    arr = []
    
    for i in range(N):
        command = input().split()
        action = command[0]
        if (action == 'insert'):
            arr.insert(int(command[1]) , int(command[2]))
        if (action == 'print'):
            print(arr)
        if (action == 'remove'):
            arr.remove(int(command[1]))
        if (action == 'append'):
            arr.append(int(command[1]))
        if (action == 'sort'):
            arr.sort()
        if (action == 'pop'):
            arr.pop() 
        if (action == 'reverse'):
            arr.reverse()                   
