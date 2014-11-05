import string
f = open ('C:\Users\Barry\Desktop\MSFT/vendingmachine\input.txt', 'r')
data = []

for line in f:
    cache = line.split(',')
    for i in range(len(cache)):
        cache[i] = cache[i].strip().replace('"','').lower()
    data.append(cache)

inventory = dict.fromkeys(list(string.ascii_lowercase),dict.fromkeys(['1','2','3','4','5','6','7','8','9'],None))
j = 0
while data[j][0][0]!= '$':
    inventory[data[j][0][0]][data[j][0][-1]] = [data[j][1],float(data[j][2]),int(data[j][3])]
    j+=1
change = {}
while data[j][0] != 'actions':
    change[data[j][0]] = [float(data[j][1]),int(data[j][2])]
    j+=1
actions = data[-1][1:]
for i in range(len(actions)):
    
#for i in range(len(inventory)):
#    print
#print '$$, total'
