# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

stamp_set = set()

for i in range(N):
    country = input()      
    stamp_set.add(country) 

print(len(stamp_set))
