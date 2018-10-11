def problem16(p):
    """int->int"""
    #calcule la somme des chiffres constituant un nombre p
    somme=0
    l=str(p)
    for k in l:
        s=s+int(k)
    return s
    
#jeudetest
assert(problem16(2**15==26)
print (problem16(2**1000))


