abecedario = [chr(i) for i in range(ord('a'), ord('z')+1)]

abecedario_filtrado = [letra for indice, letra in enumerate(abecedario, start=1) if indice % 3 != 0]

print(abecedario_filtrado)

    
    
    
