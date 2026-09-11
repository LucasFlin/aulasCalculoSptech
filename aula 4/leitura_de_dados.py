import pandas as pd

dados = pd.read_csv("/home/lucasflin/aulasCalculoSptech/aula 4/dados_maquina.csv", parse_dates=["Quando foi Coletado"])
# Por algum motivo ele só encontrou o arquivo com o caminho completo, então se for testar precisa mudar

mediaProcessador = dados["cpu total(%)"].mean()
mediaRAM = dados["ram(%)"].mean()
mediaDisc = dados["disco(%)"].mean()
mediaRedeE = dados["Rede recebida(Mbps)"].mean()
mediaRedeR = dados["Rede enviada(Mbps)"].mean()

picoProcessador = dados.sort_values(by=["cpu total(%)"]).max()

dadosMaisRecentes = dados.sort_values(by=["Quando foi Coletado"]).max()["cpu total(%)"]

print(f'''

Máquina utilizando maior processamento: {picoProcessador["Nome"]} (CPU: {picoProcessador["cpu total(%)"]}% | RAM: {picoProcessador["ram(%)"]}%)

Processamento médio entre as máquinas:
    - CPU: {mediaProcessador:.1f}%
    - RAM: {mediaRAM:.1f}%
    - Disco: {mediaDisc:.1f}%
    - Rede: {mediaRedeE:.2f} Mbps recebidos / {mediaRedeE:.2f} Mbps enviados
    
''')