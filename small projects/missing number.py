nstorage = []
n1storage = []
n = int(input())

for i in range(1,n+1):
    nstorage.append(i)

while len(n1storage) != n-1:
    n1 = int(input())
    if n1 not in n1storage and n1 >= 1 and n1 <= n:
        n1storage.append(n1)

for i in n1storage:
    if i in nstorage:
        nstorage.remove(i)

print(nstorage[0])