import socket
import sys
import time

def scan_range(ip, porta_inicio, porta_fim):
    print(f"Começar scaneamento em {ip} (Portas {porta_inicio} a {porta_fim}).\n")
    
    # Marca o tempo inicial
    tempo_inicio = time.time()
    portas_abertas = 0
    portas_fechadas = 0
    
    # Para guardar as portas e poder salvar em um .txt para depois
    lista_portas_abertas = []
    
    for porta in range(porta_inicio, porta_fim + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        s.settimeout(0.5) # Menor tempo para não travarem o programa em uma leitura demorada.
        resultado = s.connect_ex((ip, porta))
        
        if resultado == 0:
            print(f"[+] Porta {porta} ABERTA")
            portas_abertas += 1
            lista_portas_abertas.append(porta) # Salva a porta encontrada na lista
        else:
            portas_fechadas += 1
        s.close()
        
    tempo_fim = time.time()
    duracao_total = tempo_fim - tempo_inicio # Calcula o tempo da duração
    
    # Formata o resumo em uma variável para podermos imprimir e salvar no arquivo
    resumo = (
        "\n" + "="*30 + "\n"
        "      Informações da Varredura      \n"
        + "="*30 + "\n"
        f"Total de portas ABERTAS:  {portas_abertas}\n"
        f"Total de portas FECHADAS: {portas_fechadas}\n"
        f"Tempo total gasto:        {duracao_total:.2f} segundos\n"
        + "="*30
    )
    
    # Exibe o resumo no terminal
    print(resumo)

    # Pergunta se deseja salvar 
    resposta = input("\nDeseja salvar o resultado em um arquivo .txt? (S/N): ").strip().upper()
    
    if resposta == 'S':
        # Cria um nome de arquivo baseado no IP (ex: scan_127_0_0_1.txt)
        nome_arquivo = f"scan_{ip.replace('.', '_')}.txt"
        
        try:
            # Abre (ou cria) o arquivo em modo de escrita ('w')
            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write(f"Alvo: {ip}\n")
                arquivo.write(f"Range escaneado: {porta_inicio} a {porta_fim}\n\n")
                arquivo.write("Portas Abertas Encontradas:\n")
                
                for p in lista_portas_abertas:
                    arquivo.write(f"[+] Porta {p} ABERTA\n")
                    
                arquivo.write(resumo)
                
            print(f"[*] Resultados salvos com sucesso no arquivo '{nome_arquivo}'!")
            
        except Exception as e:
            print(f"[!] Erro ao tentar salvar o arquivo: {e}")

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
