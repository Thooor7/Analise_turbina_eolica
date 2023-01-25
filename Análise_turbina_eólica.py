#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# ## Ler arquivo

# In[10]:


turbina = pd.read_csv('T1.csv')

#redefinindo nome das colunas
turbina.columns = ['Data/Hora', 'ActivePower(kw)', 'WindSpeed(m/s)', 'CurvaTeórica(kwh)', 'DirecaoVento(°)']

del turbina['DirecaoVento(°)']

# Alterando tipo do dado
turbina['Data/Hora'] = pd.to_datetime(turbina['Data/Hora'])
display(turbina)


# ## Plotando os dados em um gráfico

# In[11]:


# estrutura: sns.scatterplot(data=nome da tabela aqui, x= 'coluna aqui', y= 'coluna aqui')
sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'ActivePower(kw)')


#    ## Plotando os dados em um gráfico - Teórica

# In[12]:


sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'CurvaTeórica(kwh)')


# ## Criando limites "aceitáveis"

# In[46]:


#Pegar uma vareável como potencial real e atribuir o 'ActivePower(kw)' a ela e transformar em lista
pot_real = turbina['ActivePower(kw)'].tolist()
# Mesma coisa com a Curva teórica
pot_teorica = turbina['CurvaTeórica(kwh)'].tolist()

# Criar lista de potência máxima e potência miníma. Sendo Máx= CurvaTeorica + 5%. Min= CurvaTeorica - 5%

pot_max = []
pot_min = []
dentro_limite = []

for potencia in pot_teorica:
    pot_max.append(potencia*1.05)
    pot_min.append(potencia*0.95)
    
for p, potencia in enumerate(pot_real):
    if potencia>=pot_min[p] and potencia<=pot_max[p]:
        dentro_limite.append('Dentro')
    elif potencia == 0:
        dentro_limite.append('Zero')
    else:
        dentro_limite.append('Fora')
        
print(dentro_limite.count('Dentro')/len(dentro_limite))



# ## Adicionando lista "dentro_limite" ao dataframe:

# In[48]:


turbina['DentroLimite'] = dentro_limite
display(turbina)


# ## Plotando novamente o gráfico

# In[57]:


#criando paleta de cores
cores = {'Dentro':'blue', 'Fora':'red', 'Zero':'orange'}
# 'hue' parametro para separar por cores. 's' define tamanho das bolinhas do gráfico. 'palette' é para aplicar o parametro de cores.
sns.scatterplot(data=turbina, x= 'WindSpeed(m/s)', y= 'ActivePower(kw)', hue='DentroLimite', s=1, palette=cores)


# In[ ]:




