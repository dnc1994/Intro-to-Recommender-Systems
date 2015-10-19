with open('A1.csv', 'r') as f:
    lines = f.readlines()
    
ratings = [line.strip() for line in lines[1:]]

num = [0] * 20

for rating in ratings:
    #print rating.split(',')
    for (id, rt) in enumerate(rating.split(',')[1:]):
        num[id] += (1 if rt else 0)
        
ret = zip(lines[0].split(',')[1:], num)
print sorted(ret, key=lambda x: x[1], reverse=True)[:5]