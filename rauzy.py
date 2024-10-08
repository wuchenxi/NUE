from fractions import Fraction

#continued fraction calculation
def contfrac(l):
    r=Fraction(0, 1)
    rl=[l[-i] for i in range(1, len(l))]
    for a in rl:
        r=1/(a+r)
    return r+l[0]

def num2contfrac(q):
    a=q.numerator
    b=q.denominator
    r=[a//b]
    a=a%b
    while a>0:
        r+=[b//a]
        c=b%a
        b=a
        a=c
    return r

lst=[i*i for i in range(1, 51)]

alpha=contfrac(lst)

for k in range(10):
    r=contfrac(lst[:k+1])
    print(k+1, r.numerator, r.denominator)


gamma=Fraction(0, 1)
for i in range(1, 26):
    r=contfrac(lst[:2*i])
    gamma+=Fraction(2, 1)*(r.numerator-r.denominator*alpha)

print(float(alpha), float(gamma))
print(num2contfrac(alpha), num2contfrac(gamma))
#gamma is the length of slit

#y=(2, [1, 0], [2-alpha, alpha-1])
#y=(6, [2, 3, 1, 5, 0, 4], [gamma, 1-alpha-gamma, alpha, gamma, 1-alpha-gamma, alpha])
y=(3, [2, 0, 1], [gamma, 2-alpha-gamma, alpha-1])


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
        #print("l", lengths)
        newlengths=lengths[:-1]+[lengths[-1]-lengths[perm[-1]]]
        #print("nl:", newlengths)
        new_perm=[]
        for i in perm[:-1]:
            if i==n-1:
                new_perm+=[i, perm[-1]]
            else:
                new_perm+=[i]
        return 2, (n, new_perm, newlengths)
    else:
        new_perm=[]
        for i in perm[:-1]:
            if i==n-1:
                new_perm+=[perm[-1]]
            else:
                new_perm+=[i]
        return 0, (n-1, new_perm, lengths[:-1])

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
    if flag==0:
        print(steps, flag, y[0], y[1], [num2contfrac(x) for x in y[2]])
    sequence+=[flag]
    if y[0]==1:
        break
print(summary(sequence))
print(steps)
