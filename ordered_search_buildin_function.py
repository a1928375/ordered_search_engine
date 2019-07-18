ranks={'http://udacity.com/cs101x/urank/kathleen.html': 0.1166, \
'http://udacity.com/cs101x/urank/zinc.html': 0.0387, \
'http://udacity.com/cs101x/urank/hummus.html': 0.0387, \
'http://udacity.com/cs101x/urank/arsenic.html': 0.0541, \
'http://udacity.com/cs101x/urank/index.html': 0.0333, \
'http://udacity.com/cs101x/urank/nickel.html': 0.0974}

index={'Nickel': ['http://udacity.com/cs101x/urank/nickel.html'], 'href="http://udacity.com/cs101x/urank/hummus.html">': ['http://udacity.com/cs101x/urank/index.html'], 'Kathleen': ['http://udacity.com/cs101x/urank/kathleen.html'], 'Cooking': ['http://udacity.com/cs101x/urank/index.html'], 'href="http://udacity.com/cs101x/urank/kathleen.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/nickel.html'], 'href="http://udacity.com/cs101x/urank/arsenic.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html'], 'Hummus': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/kathleen.html', 'http://udacity.com/cs101x/urank/arsenic.html', 'http://udacity.com/cs101x/urank/arsenic.html', 'http://udacity.com/cs101x/urank/hummus.html', 'http://udacity.com/cs101x/urank/hummus.html'], 'Zinc': ['http://udacity.com/cs101x/urank/zinc.html'], '<a': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/arsenic.html'], 'href="http://udacity.com/cs101x/urank/nickel.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/arsenic.html'], 'href="http://udacity.com/cs101x/urank/zinc.html">': ['http://udacity.com/cs101x/urank/index.html'], 'Arsenic': ['http://udacity.com/cs101x/urank/arsenic.html']}

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

L=lookup(index,"Hummus")
H=[]
g=len(L)
i=0
M=[]

while i<g:
    b=L.pop(0)
    if b not in L:
        L.append(b)
    i=i+1
 
for i in L:
    H.append([i,ranks[i]])

print H

def takeSecond(elem):
    return elem[1]
    
H.sort(key=takeSecond,reverse=True)

for s in H:
    M.append(s[0])

print M
