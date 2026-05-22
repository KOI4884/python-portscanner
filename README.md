# Python Port Scanner 🕵️‍♂️🔍

Um scanner de portas TCP leve, rápido e eficiente desenvolvido totalmente em Python. Este projeto utiliza a biblioteca nativa `socket` para realizar o "Three-way Handshake" e verificar o status de portas em um endereço IP alvo.

## 🚀 Funcionalidades

- **Scanner Básico (Porta Única):** Verifica rapidamente se uma porta específica está aberta ou fechada.
- **Scanner de Range (Múltiplas Portas):** Varre um intervalo completo de portas sequencialmente (ex: 1 a 8080).
- **Tratamento de Timeout:** Evita travamentos em portas filtradas, mantendo a varredura ágil.
- **Exportação de Resultados:** Opção interativa no final da execução para salvar o relatório completo (portas abertas e estatísticas) em um arquivo `.txt`.
- **Resumo Detalhado:** Exibe o total de portas abertas, fechadas e calcula o tempo exato gasto na operação.
- **Precisão Absoluta:** Diferente da configuração padrão de outras ferramentas de mercado (que focam apenas nas top 1000 portas), este script verifica literalmente todas as portas do range solicitado.

## 🎥 Demonstração

Veja o funcionamento do script gerando logs e salvando os resultados:

https://github.com/user-attachments/assets/70f214fc-164f-4c01-8e3e-dc174084d733

## 🛠️ Pré-requisitos

Tudo o que você precisa é ter o [Python 3.x](https://www.python.org/downloads/) instalado na sua máquina. Nenhuma biblioteca externa é necessária (dependências zero).

## 💻 Como usar

Pelo terminal, navegue até a pasta onde o script está salvo e execute o comando abaixo.

### Sintaxe Básica
Para escanear várias portas, passe o IP alvo e o intervalo desejado no formato `INICIO-FIM`:

```bash
python3 PortScanner.py <IP_ALVO> <PORTA_INICIO>-<PORTA_FIM>
```

### Exemplo de Uso
```bash
python3 PortScanner.py 127.0.0.1 1-8080
```

**Exemplo de Saída no Terminal:**
```text
Começar scaneamento em 127.0.0.1 (Portas 1 a 8080).

[+] Porta 631 ABERTA
[+] Porta 1716 ABERTA
[+] Porta 5201 ABERTA
[+] Porta 7070 ABERTA
[+] Porta 8000 ABERTA

==============================
    Informações da Varredura      
==============================
Total de portas ABERTAS:  5
Total de portas FECHADAS: 8075
Tempo total gasto:        0.38 segundos
==============================

Deseja salvar o resultado em um arquivo .txt? (S/N): S
[*] Resultados salvos com sucesso no arquivo 'scan_127_0_0_1.txt'!
```
