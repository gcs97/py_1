aparicoes = {'Carlos': 1, 'Guilherme': 1, 'cachorro': 2, 'pastel': 2, 'vindo': 1}

for chave,apari in aparicoes.items():
  print( apari, chave)
  
  
  
meu_texto = "once upon a time there was a girl from ipanema that vanished in thin air"  
meu_texto = meu_texto.lower()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0 )
    aparicoes[palavra] = ate_agora + 1

    
print(aparicoes)