def reverse(n):  #fonction qui a un nombre renvoie son palindrome
    """int->int"""
    chaine=str(n)
    return int(c[::-1])
    
assert(reverse(12==21))

def testlychrel(n):
    """int->bool"""
    p=n+reverse(n)
    L=[p]
    for k in range (0,50):
        P=L[k]+reverse(L[k])
        L.append(P)  #génère les 50 nombres issus de l'argument n
    for k in range(0,len(L)):
        if L[k]==reverse(L[k]):
            return True
    return False
    
def problem55(n):
    """int->int"""
    somme=0  
    for k in range (0,n):
        if testlychrel(k)==False:
            somme=somme+1
    return somme
    
assert
        