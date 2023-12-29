# Y6WHTVBH2KWF7ZF4F66PGQ9N

from datetime import datetime
from twilio.rest import Client
# import schedule
# import time

#  Credenciais do Twilio
account_sid = 'AC28084bb9f13b13fad8f6ce2f3c896fbf'
auth_token = '2ff88b037ed101e020b0cbd24136491a'
client = Client(account_sid, auth_token)

remetente = 'whatsapp:+14155238886' # numero dado pelo twilio
destinatario = 'whatsapp:+5519999024890' # numero que sera enviado

def enviar_mensagem():

    # Data do dia
    hoje = datetime.now()

    # aluguel alfenas
    if hoje.day == 5:
        # Enviar mensagem no WhatsApp
        mensagem = client.messages.create(
            body='Bom dia, lindão!\nHoje é dia 6, dia de pagar aluguel em Alfenas',
            from_=remetente,
            to=destinatario
        )

    # garagem alfenas
    if hoje.day == 16:

        # Enviar mensagem no WhatsApp
        mensagem = client.messages.create(
            body='Bom dia, lindão!\nHoje é dia 16, dia de pagar a garagem em Alfenas\n\nContato salvo como: *Estacionamento Alfenas*\nChave pix (CNPJ): *11.216.963.0001.43*\nNome: *V. Miranda Andrade*',
            from_=remetente,
            to=destinatario
        )

        mensagem2 = client.messages.create(
            body='11.216.963.0001.43',
            from_=remetente,
            to=destinatario
        )

    # Academia
    # Depois ve o dia que realmente paga e muda
    if hoje.day == 6:

        # Enviar mensagem no WhatsApp
        mensagem = client.messages.create(
            body='Dia de pagar academia Alfenas',
            from_=remetente,
            to=destinatario
        )

enviar_mensagem()

# schedule.every().day.at("08:00").do(enviar_mensagem)

# Loop infinito para continuar a execução do código
        
'''
while True:
    agora = datetime.now().strftime('%H:%M')
    cont = 0
    while agora == '08:00' and cont == 0:
        # Verificar se a hora atual é 08:00
        
        enviar_mensagem()

        # Verificar se há tarefas agendadas no schedule  
        schedule.run_pending()
        time.sleep(61)
        cont = 1
'''


    