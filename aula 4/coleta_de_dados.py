import psutil
import csv
import time

with open('./dados_coletados.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['Timestamp', 'CPU', 'RAM', 'Disco'])
    for i in range(10):
        cpu = psutil.cpu_percent(interval=None)
        ram = psutil.virtual_memory().percent
        disco = psutil.disk_usage('/').percent
        tempoA = time.localtime()
        tempoF = time.strftime(f"%I:%M:%S - %d/%m/%Y")
        txtCPU = str(cpu)
        txtRAM = str(ram)
        txtDisco = str(disco)

        writer.writerow([tempoF, txtCPU, txtRAM, txtDisco])

        print(cpu)
        print(ram)
        print(disco)
        print(tempoF)
        
        time.sleep(10)
