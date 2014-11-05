import string
f = open ('input.txt', 'r')
data = []
for line in f:
    cache = line.split(',')
    for i in range(len(cache)):
        cache[i] = cache[i].strip().replace('"','').lower()
    data.append(cache)
letter_key = list(string.ascii_lowercase )
print data
for i in range(len(data)):
    dict1 = dict.fromkeys(letter_key, 0)
    dict2 = dict.fromkeys(letter_key, 0)
    for j in range(len(data[i][0])):
        if data[i][0][j].isalpha():
            dict1[data[i][0][j]] += 1    
    for j in range(len(data[i][1])):
        if data[i][1][j].isalpha():
            dict2[data[i][1][j]] += 1 
    if dict1 == dict2:
        print "Valid Pattern"
    else:
        print "Invalid Pattern"