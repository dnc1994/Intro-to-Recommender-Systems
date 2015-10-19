with open('A1.csv', 'r') as f:
    lines = f.readlines()
    
ratings = [line.strip() for line in lines[1:]]

num = [0] * 20
user = [0] * 20

for (uid, rating) in enumerate(ratings):
    #print rating.split(',')
    for (id, rt) in enumerate(rating.split(',')[1:]):
        if id == 0 and rt:
            user[uid] = 1

tot = len(filter(bool, user))
            
for (uid, rating) in enumerate(ratings):
    if not user[uid]:
        continue
    for (id, rt) in enumerate(rating.split(',')[1:]):
        num[id] += (1 if rt else 0)
        
ret = zip(lines[0].split(',')[1:], [num[i] / float(tot) for i in range(20)])
print sorted(ret, key=lambda x: x[1], reverse=True)[:6]