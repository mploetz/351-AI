# -*- coding: utf-8 -*-
"""
B351 - Assignment0 skeleton code
"""
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)
#**** Your Code goes here ****

def name_number():
    
    name = 'Matthew Ploetz'
    number = '0003115702'
    return name,number

def remove_dup(l):
    #l indicates input list
    l2 = []
    for x in l:
        if x not in l2:
            l2.append(x)
    return l2

def substring(a,i,l):
    #a indicates character to be inserted
    #i indicates index position
    #l indicates list
    l2 = []
    j = 0
    if (i > len(l)):
        l.append(a)
        return l
    else:
        for x in l:
            if (j == i-1):
                l2.append(x)
                l2.append(a)
                j += 1
            else:
                l2.append(x)
                j += 1
    return l2
  
    

def diag_add(d,l):
        
    #d = dimension of the square matrix
    #l = matrix values
    leading = 0
    tailing = 0
    newD = 0
    newD2 = d-1
    while(True):
        if (newD > len(l) or newD2 > len(l)):
            return (leading, tailing)
        leading += l[newD]
        newD += d+1
        tailing += l[newD2]
        newD2 += d-1
    return (leading, tailing)
          
#****  End of your Code ****

#**** You can manually change the input to the functions below and test your codes****

def main():   
    
    assert(compare(remove_dup(['a','c','a']),['c','a']))
    assert(compare(remove_dup([10,100,10000,10,100,10]),[10,100,10000]))
    print ("Test cases passed for Remove Duplicates")
    
    
    assert (substring('d',10,['a','b','c'])==['a','b','c','d'])
    assert (substring('a', 2, ['c', 'd', 'b'])==['c','d','a','b'])
    print ("Test cases passed for Substring")
        
    assert (diag_add(3,[2,2,2,2,2,2,2,2,2]) == (6,6))
    assert (diag_add(3,[1, 2, 3, 10, 12, 15, 20, 22, 25]) == (38,35))
    print ("passed all cases")        
    
            
main()
        
#**** All the best ****
    
    
