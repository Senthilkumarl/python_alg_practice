inp=input('')
ovl='aeiou'

inx=[0,4,8,14,20]
rt=[]
for c in inp:
    if c in ovl:
        rt.append(chr(ord(c) + 1))
        #print(c,'ovl',rt)
    elif c in 'bcd':
        rt.append(ovl[1])
    elif c in 'fgh':
        rt.append(ovl[2])
    elif c in 'jklmn':
        rt.append(ovl[3])
    elif c in 'pqrst':
        rt.append(ovl[4])
    elif c in 'vwxyz':
        rt.append(ovl[0])
    
        
print(''.join(rt))
