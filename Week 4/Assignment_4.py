def rainaverage(l):
    (t1,t2,t3) = ({},{},{})
    for i,j in l:
        if i not in t1:
            (t1[i],t2[i]) = (j,1)
        else:
            (t1[i],t2[i]) = (t1[i]+j,t2[i]+1)
    for i,j in t2.items():
        t3[i] = float(t1[i]/j)
    temp = [(i,j) for i,j in t3.items()]
    temp.sort(key=lambda a:a[0])
    return temp

temp = []

def flatten(l):
    for i in l:
        if type(i) == int:
            temp.append(i)
        elif type(i) == list:
            flatten(i)
        elif type(i) == tuple:
            temp.append(i)
        else:
            temp.append(i)
    return temp
