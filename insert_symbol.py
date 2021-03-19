palavra = 'socorro'
res='|'.join(palavra[i:i + 1] for i in range(0, len(palavra), 1))
print(res)