
import pandas as pd
import matplotlib.pyplot as plt

#Carregando os dados
df = pd.read_csv('gasolina.csv')

# Plotando dados
plt.figure(figsize=(8, 6))
plt.plot(df['dia'], df['venda'], marker='o', linestyle='-')
plt.title('Variação do Preço da Gasolina ao Longo dos Dias')
plt.xlabel('Dia')
plt.ylabel('Preço (R$)')
plt.grid(True)

#salvando grafico
plt.savefig('gasolina.png')
plt.show()
