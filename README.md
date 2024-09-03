# door_scanner
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

