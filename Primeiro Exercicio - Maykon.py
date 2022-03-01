#!/usr/bin/env python
# coding: utf-8

# # <font color='purple'>Data Science Academy - Python Fundamentos - Capítulo 2</font>
# 

# In[ ]:


# Versão da Linguagem Python
from platform import python_version
print('Versão da Linguagem Python Usada Neste Jupyter Notebook:', python_version())


# ## Exercícios Cap02

# In[ ]:


# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.


# In[1]:


lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)


# In[23]:


# Exercício 2 - Crie uma lista de 6 objetos e imprima na tela
lista=["Maykon","Duda","Manu","Aline","Maria","Conha"]
print(lista)


# In[18]:


# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string= "Vou concatenar "
string2= "beleza fera"
frase_final= string+string2
print(frase_final)


# In[19]:


# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla

tupla1 = (1,2,2,3,4,4,4,5)
tupla1.count(4)


# In[20]:


# Exercício 5 - Crie um dicionário vazio e imprima na tela
dicio = {}
print(dicio)


# In[21]:


# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dicio = {'chuva':'gotas', 'sol':'calor', 'praia':'mar'}
print (dicio)


# In[22]:


# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dicio['Ceu'] = 'azul'
print (dicio)


# In[25]:


# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dicio = {'K1':'Marreta', 'K2': 'FACÃO', 'KIT3' : [7,8]}
print (dicio)


# In[26]:


# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dicionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
list = ["String", (7,8), {'chave1':'valor1', 'chave2': 'valor2'}, 88.88] 
print (list)


# In[30]:


# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
frase[0:18]


# # Fim

#     Se houver algum erro, por favor me informar. Sou iniciante. Valeu!

# 
