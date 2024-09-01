
import matplotlib.pyplot as plt
import pandas as pd

# Carregando os dados
df = pd.read_csv('gasolina.csv')

# Plotando dados
plt.figure(figsize=(8, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-', color='darkgreen', label='Preço da Gasolina') # alterrei cor verde na linha

# Ajustando o título para negrito e adicionando a legenda
plt.title('Variação do Preço da Gasolina ao Longo dos Dias', fontweight='bold') #adicionando negrito no titulo
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

# Salvando o gráfico
plt.savefig('gasolina.png')
plt.show()
