# port_probe
Este script realiza a varredura de portas em um determinado host, verificando quais portas estão abertas e tentando identificar o serviço associado a cada uma delas. O script é multi-threaded, o que permite uma varredura rápida. Ele também utiliza cores e efeitos visuais para tornar a saída no terminal mais informativa e agradável

Funcionalidades
Varredura de portas: Verifica as portas de 1 a 65.000 em um host específico.
Identificação de serviços: Tenta identificar o serviço em execução em cada porta aberta.
Multi-threading: Utiliza 100 threads para realizar a varredura de portas de forma mais eficiente.
Feedback visual: Utiliza cores para destacar informações importantes, como portas abertas e erros.
Centralização de textos: O banner e a informação "Powered by foryousec.com" são centralizados na tela.
Resumo e Log: Gera um resumo ao final da varredura e salva os resultados em um arquivo de log.

Requisitos
O script requer Python 3.x e algumas bibliotecas adicionais. As bibliotecas necessárias estão listadas no arquivo requirements.txt. Você pode instalá-las usando o comando:
pip install -r requirements.txt

Multi-threading
O script utiliza a biblioteca threading para criar múltiplas threads que escaneiam as portas em paralelo. A fila (queue.Queue) garante que as threads não verifiquem as mesmas portas ao mesmo tempo. O uso de threading.Lock evita conflitos ao acessar recursos compartilhados, como a impressão de resultados no terminal.

Barra de Progresso
A barra de progresso (tqdm) é usada para fornecer feedback visual ao usuário sobre o andamento do escaneamento, atualizando conforme as portas são processadas.
Ao final da execução, um resumo das portas abertas é exibido, e os resultados completos são salvos em um arquivo de texto.
