from fractions import Fraction

#continued fraction calculation
def contfrac(l):
    r=Fraction(0, 1)
    rl=[l[-i] for i in range(1, len(l)+1)]
    for a in rl:
        r=1/(a+r)
    return r

lst=[i*i for i in range(1, 51)]

alpha=contfrac(lst)

rotation=(2, [1, 0], [1-alpha, alpha])

gamma=Fraction(0, 1)
for i in range(1, 26):
    r=contfrac(lst[:2*i+1])
    gamma+=Fraction(2, 1)*(r.numerator-r.denominator*alpha)

print(float(alpha), float(gamma))

#gamma is the length of slit

y=(6, [3, 2, 1, 0, 5, 4], [gamma, 1-alpha-gamma, alpha, gamma, 1-alpha-gamma, alpha])

#Rauzy induction
def induction(ifs):
    n=ifs[0]
    perm=ifs[1]
    lengths=ifs[2]
    if lengths[n-1]<lengths[perm[-1]]:
        split_id=perm[-1]
        newlengths=lengths[:split_id]+[lengths[split_id]-lengths[-1], lengths[-1]]+lengths[split_id+1:-1]
        new_perm=[]
        for i in perm:
            if i<=split_id:
                new_perm+=[i]
            elif i==n-1:
                new_perm+=[split_id+1]
            else:
                new_perm+=[i+1]
        return 1, (n, new_perm, newlengths)
    elif lengths[n-1]>lengths[perm[-1]]:
        newlengths=lengths[:-1]+[lengths[-1]-lengths[perm[-1]]]
        new_perm=[]
        for i in perm[:-1]:
            if i==n-1:
                new_perm+=[i, perm[-1]]
            else:
                new_perm+=[i]
        return 2, (n, new_perm, newlengths)
    else:
        return 0, ifs

sequence=[]

def summary(sequence):
    r=[]
    cur=0
    count=0
    for i in sequence:
        if i!=cur:
            if cur!=0:
                r+=[count]
            cur=i
            count=1
        else:
            count+=1
    return r

steps=0
while(True):
    flag, y=induction(y)
    steps+=1
    sequence+=[flag]
    if flag==0:
        break
print(summary(sequence))
print(steps)
