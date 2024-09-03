import sys
import os
import socket
import pyfiglet
import threading
import time
import colorama
import logging
from datetime import datetime
from colorama import *
from tqdm import tqdm
from queue import Queue
from shutil import get_terminal_size

logging.basicConfig(filename='port_scanner.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:  
        os.system('clear')

def center_text(text):
    terminal_width = get_terminal_size().columns
    return text.center(terminal_width)

def scan_port(port, progress_bar):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        r = s.connect_ex((target_ip, port))
        if r == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Desconhecido"
            with print_lock:
                print(Fore.GREEN + " [+]  " + Fore.WHITE + str(port) + Fore.WHITE + f" ==> " + Fore.LIGHTCYAN_EX + "Aberta! Serviço: " + Fore.LIGHTYELLOW_EX + f"{service}" + Fore.RESET)
                open_ports.append((port, service))
        s.close()
    except socket.error as e:
        with print_lock:
            print(Fore.YELLOW + f" [!] Erro ao escanear a porta {port}: {e}" + Fore.RESET)
        logging.error(f"Erro ao escanear a porta {port}: {e}")
    except Exception as e:
        with print_lock:
            print(Fore.YELLOW + f" [!] Erro inesperado: {e}" + Fore.RESET)
        logging.error(f"Erro inesperado ao escanear a porta {port}: {e}")
    finally:
        progress_bar.update(1) 


def threader(progress_bar):
    while True:
        worker = q.get()
        scan_port(worker, progress_bar)
        q.task_done()

colorama.init()
print_lock = threading.Lock()
open_ports = []

clear_screen()
logo = pyfiglet.figlet_format("PORT SCANNER")
print(Fore.LIGHTBLUE_EX + center_text(logo) + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "-" * 70 + Fore.RESET)
print("                               foryousec.com")
print(Fore.LIGHTGREEN_EX + "-" * 70 + Fore.RESET) 

print(Fore.LIGHTCYAN_EX + "\n  BEM VINDO AO PORT SCANNER!\n" + Fore.RESET)

try:
    target = input(Fore.LIGHTYELLOW_EX + "  Digite o HOST para realizar o scanner: " + Fore.RESET)
    target_ip = socket.gethostbyname(target)
    logging.info(f"Alvo: {target} ({target_ip})")
    time.sleep(1)
except Exception:
    print("\n" + Fore.RED +  "Erro: não foi possível encontrar o HOST. (Verifique sua conexão com a Internet ou sua entrada está errada)")
    logging.error("Erro ao resolver o nome do host.")
    sys.exit()

print(Fore.LIGHTGREEN_EX + "-" * 60 + Fore.RESET)
print(Fore.LIGHTMAGENTA_EX + "Aguarde, verificando o host... ==>  " + Fore.LIGHTBLUE_EX + target_ip + Fore.RESET)
time.sleep(2)
print(Fore.LIGHTGREEN_EX + "\nVai demorar um pouco, tome um cafezinho :)\n" + Fore.RESET)
time.sleep(1)
print(Fore.LIGHTRED_EX + 'A digitalização começou: ')
print(Fore.LIGHTYELLOW_EX + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "\n" + "-" * 60 + "\n" + Fore.RESET)

q = Queue()
n_threads = 100

progress_bar = tqdm(total=65000, desc=Fore.LIGHTBLUE_EX + "Scanning Ports", ncols=100, miniters=1)

for x in range(n_threads):
    t = threading.Thread(target=threader, args=(progress_bar,))
    t.daemon = True
    t.start()

for port in range(1, 65001):
    q.put(port)

q.join()
progress_bar.close()

print(Fore.LIGHTGREEN_EX + "\nVerificação concluída." + Fore.RESET)
print(Fore.LIGHTBLUE_EX + "Total de portas abertas: " + Fore.LIGHTRED_EX + str(len(open_ports)) + Fore.RESET)
print(Fore.LIGHTGREEN_EX + "Confira os resultados acima." + Fore.RESET)

output_file = f"scan_results_{target}.txt"
with open(output_file, 'w') as f:
    f.write("Porta\tStatus\n")
    for port, service in open_ports:
        f.write(f"{port}\tAberta - Serviço: {service}\n")
print(Fore.LIGHTGREEN_EX + f"\nResultados salvos em {output_file}" + Fore.RESET)

print(Fore.LIGHTCYAN_EX + "\nObrigado por usar o Port Scanner! Até a próxima!" + Fore.RESET)
logging.info("Verificação concluída.")
