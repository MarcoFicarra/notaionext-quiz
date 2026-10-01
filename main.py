# --- FUNZIONE SALVATAGGIO EXCEL ---
def salva_su_excel(nome_studio, nome_notaio, email, telefono, luogo, totale, profilo, area_prioritaria):
    file_excel = "risultati_quiz.xlsx"
    data_ora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        if not os.path.exists(file_excel):
            wb = Workbook()
            ws = wb.active
            ws.title = "Leads Quiz"
            ws.append(["Data/Ora", "Nome Studio", "Nome Notaio", "Email", "Telefono", "Luogo", "Punteggio Totale", "Profilo", "Area Prioritaria"])
        else:
            wb = load_workbook(file_excel)
            ws = wb.active

        ws.append([data_ora, nome_studio, nome_notaio, email, telefono, luogo, totale, profilo, area_prioritaria])
        wb.save(file_excel)
    except Exception as e:
        print(f"Errore durante la scrittura su Excel: {e}")

# --- FUNZIONE NOTIFICA EMAIL GMAIL ---
def invia_email_notifica(nome_studio, nome_notaio, email_cliente, telefono, luogo, totale, profilo, area_prioritaria):
    mittente = "notaionextwki@gmail.com"
    password = "TUA_PASSWORD_DI_16_LETTERE_GENERATA"  # <-- Inserisci qui le 16 lettere senza spazi
    destinatario = "notaionextwki@gmail.com"
    server_smtp = "smtp.gmail.com"
    porta_smtp = 587

    msg = MIMEMultipart()
    msg['From'] = mittente
    msg['To'] = destinatario
    msg['Subject'] = f"Nuovo Lead Quiz NotaioNext: {nome_studio} - {nome_notaio}"

    corpo = f"""
    Un nuovo utente ha completato il check-up su NotaioNext!

    DETTAGLI STUDIO:
    --------------------------------------------------
    Nome Studio: {nome_studio}
    Nome Notaio: {nome_notaio}
    Email Utente: {email_cliente}
    Telefono: {telefono}
    Luogo: {luogo}

    ESITO CHECK-UP:
    --------------------------------------------------
    Punteggio Totale: {totale} / 25
    Profilo Risultante: {profilo}
    Area Prioritaria da Intervenire: {area_prioritaria}

    Data compilazione: {datetime.now().strftime("%d/%m/%Y %H:%M")}
    --------------------------------------------------
    I dati sono stati salvati automaticamente anche nel file Excel 'risultati_quiz.xlsx' sul server IONOS.
    """
    msg.attach(MIMEText(corpo, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP(server_smtp, porta_smtp)
        server.starttls()
        server.login(mittente, password)
        server.send_message(msg)
        server.quit()
        print("Notifica email inviata con successo!")
    except Exception as e:
        print(f"Errore durante l'invio dell'e-mail: {e}")
