import imaplib

server   = ""
user     = ""
password = ""

print("Realizando login...")

try:
    box = imaplib.IMAP4_SSL(server, 993)
    box.login(user,password)
    print("Login realizado com sucesso...")

    print("Selecionando emails na caixa de entrada...")
    box.select('INBOX')
    print("Emails selecionados com sucesso...")

    print("Procurando emails não lidos na caixa de entrada...")
    typ, data = box.search(None, 'Seen') #https://gist.github.com/martinrusev/6121028

    contEmailsExcluidos = 0


    print("Marcando emails para exclusão...")
    for num in data[0].split():
        box.store(num, '+FLAGS', '\\Deleted')
        contEmailsExcluidos += 1


    print("Marcação concluída...\n Foram marcados %s emails para exclusão." % contEmailsExcluidos)   

    print("Iniciando exclusão definitiva...")
    box.expunge()

    print("Exclusão realizada com sucesso...")
    box.close()

    print("Realizando logout no email...")
    box.logout()

    print("Logout realizado com sucesso...")

except Exception as e:
    print("Ocorreu um erro %s" % (e))

