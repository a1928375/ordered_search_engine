ranks={'http://udacity.com/cs101x/urank/kathleen.html': 0.1166, \
'http://udacity.com/cs101x/urank/zinc.html': 0.0387, \
'http://udacity.com/cs101x/urank/hummus.html': 0.0387, \
'http://udacity.com/cs101x/urank/arsenic.html': 0.0541, \
'http://udacity.com/cs101x/urank/index.html': 0.0333, \
'http://udacity.com/cs101x/urank/nickel.html': 0.0974}

index={'Nickel': ['http://udacity.com/cs101x/urank/nickel.html'], 'href="http://udacity.com/cs101x/urank/hummus.html">': ['http://udacity.com/cs101x/urank/index.html'], 'Kathleen': ['http://udacity.com/cs101x/urank/kathleen.html'], 'Cooking': ['http://udacity.com/cs101x/urank/index.html'], 'href="http://udacity.com/cs101x/urank/kathleen.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/nickel.html'], 'href="http://udacity.com/cs101x/urank/arsenic.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html'], 'Hummus': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/kathleen.html', 'http://udacity.com/cs101x/urank/arsenic.html', 'http://udacity.com/cs101x/urank/arsenic.html', 'http://udacity.com/cs101x/urank/hummus.html', 'http://udacity.com/cs101x/urank/hummus.html'], 'Zinc': ['http://udacity.com/cs101x/urank/zinc.html'], '<a': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/nickel.html', 'http://udacity.com/cs101x/urank/arsenic.html'], 'href="http://udacity.com/cs101x/urank/nickel.html">': ['http://udacity.com/cs101x/urank/index.html', 'http://udacity.com/cs101x/urank/zinc.html', 'http://udacity.com/cs101x/urank/arsenic.html'], 'href="http://udacity.com/cs101x/urank/zinc.html">': ['http://udacity.com/cs101x/urank/index.html'], 'Arsenic': ['http://udacity.com/cs101x/urank/arsenic.html']}

import random
def quicksort_pages(list):
    bigger=[]
    smaller=[]   

    if len(list)==0 or len(list)==1:
        return list
    else:
        pivot=list.pop(random.randint(0,len(list)-1))
        for i in list:
            if ranks[i]<ranks[pivot]:
                if i not in smaller:
                    smaller.append(i)
            else:
                if i not in bigger:
                    bigger.append(i)
        return quicksort_pages(bigger)+[pivot]+quicksort_pages(smaller)
        
def ordered_search(index, ranks, keyword):
    pages=lookup(index,keyword)
    if not pages:
        return None
    else:
        return quicksort_pages(pages)
    
def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

print ordered_search(index, ranks, 'Hummus')


print ordered_search(index, ranks, 'the')

print ordered_search(index, ranks, 'babaganoush')
