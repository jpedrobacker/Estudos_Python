
nomes = ['joão', 'clara', 'rafael', 'beatriz', 'joaquim', 'ana', 'vanesssa']

def len_nomes(nomes):
    tam_nomes = len(nomes)
    
    for i in range(tam_nomes):
        for j in range(i+1,tam_nomes):
            if len(nomes[i]) > len(nomes[j]):
                temp = nomes[i]
                nomes[i] = nomes[j]
                nomes[j] = temp
                
    return nomes

print (len_nomes(nomes))
print ('Hello')