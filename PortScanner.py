import socket
import sys
import time

def scan_range(ip, porta_inicio, porta_fim):
    print(f"Começar scaneamento em {ip} (Portas {porta_inicio} a {porta_fim}).\n")
    
    # Marca o tempo inicial
    tempo_inicio = time.time()
    portas_abertas = 0
    portas_fechadas = 0
    
    for porta in range(porta_inicio, porta_fim + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(0.5) # Menor tempo para não travarem o programa em uma leitura demorada.
        resultado = s.connect_ex((ip, porta))
        
        if resultado == 0:
            print(f"[+] Porta {porta} ABERTA")
            portas_abertas += 1
        else:
            portas_fechadas += 1
        s.close()
        
    tempo_fim = time.time()
    duracao_total = tempo_fim - tempo_inicio # Calcula o tempo da duração
    
    # Exibe as informaçẽos coletadas
    print("\n" + "="*30)
    print("      Informaçẽos da Varredura      ")
    print("="*30)
    print(f"Total de portas ABERTAS:  {portas_abertas}")
    print(f"Total de portas FECHADAS: {portas_fechadas}")
    print(f"Tempo total gasto:        {duracao_total:.2f} segundos")
    print("="*30)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso correto: python3 PortScanner.py <IP> <INICIO-FIM>")
        print("Exemplo: python3 PortScanner.py 192.168.1.1 1-1024")
        sys.exit(1)

    alvo_ip = sys.argv[1]
    range_portas = sys.argv[2].split('-')
    
    if len(range_portas) != 2:
        print("Formato de range inválido. Use o formato INICIO-FIM.")
        sys.exit(1)
        
    inicio = int(range_portas[0])
    fim = int(range_portas[1])
    
    scan_range(alvo_ip, inicio, fim)
