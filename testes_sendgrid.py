# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import Bcc

# ler um arquivo de anuncio e passar o conteudo do arquivo para o html_content
# ler o arquivo de endereços e adicionar o to_emails
# procurar na API limite de emails que da pra adicionar nas mensagens
# teria alguma classe diferente na api pra mandar email pra um monte de gente
# ou teria que botar isso num loop?
# maximo de 1000 recipients
# https://docs.sendgrid.com/api-reference/mail-send/limitations
# 

message = Mail(
    from_email='contas@ible.com.br',
    to_emails=['contas@ible.com.br'],
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    message.bcc = [
        Bcc(
            email='flaviohpo@yahoo.com',
            name="Friendly Flavio",
            p=0
        ),
        Bcc(
            email='flaviohenriquepereiraoliveira@gmail.com',
            name="Friendlyyyy Flavio",
            p=0
        )
    ]
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
