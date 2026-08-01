from flask import Flask, request
import subprocess
import requests
import os

app = Flask(__name__)

@app.route('/io', methods=["POST"])
def record_live():
    # Riceve i dati in formato testuale
    contenuto = request.get_data(as_text=True)
    print('Payload ricevuto:', contenuto)
    
    try:
        # Estrazione dell'username (adatta questa logica al formato esatto che ti invia Tasker)
        # Qui manteniamo la tua logica originale che cerca l'username tra gli apici
        username = contenuto.split(" ")[0].split("'")[1]
    except IndexError:
        print('Errore: Impossibile fare il parsing del nome utente dalla notifica.')
        return 'Errore di parsing', 400
        
    print(f'Username estratto: {username}')

    # 1. Invia notifica IFTTT in modo sicuro usando le variabili d'ambiente
    ifttt_key = os.getenv('IFTTT_WEBHOOK_KEY')
    if ifttt_key:
        dictToSend = {'value1': f'START REC LIVE: {username}'}
        ifttt_url = f'https://maker.ifttt.com/trigger/avviso/with/key/{ifttt_key}'
        try:
            requests.post(ifttt_url, json=dictToSend)
            print('Notifica IFTTT inviata.')
        except requests.exceptions.RequestException as e:
            print(f"Errore nell'invio della notifica IFTTT: {e}")
    else:
        print("Chiave IFTTT non configurata. Notifica saltata.")

    # 2. Esecuzione SICURA di PyInstaLive
    # Utilizziamo subprocess.run con una lista per prevenire Command Injection
    try:
        print(f"Avvio registrazione per {username}...")
        
        # Esecuzione sicura: i parametri sono isolati e non passati ad una shell bash
        result = subprocess.run(
            ['python', '-m', 'pyinstalive', '-d', username],
            capture_output=True,
            text=True
        )
        
        print("Output PyInstaLive:\n", result.stdout)
        if result.stderr:
            print("Avvisi/Errori PyInstaLive:\n", result.stderr)
            
    except Exception as e:
        print(f"Errore imprevisto durante l'avvio di PyInstaLive: {e}")
        return 'Errore del server durante la registrazione', 500

    return f'Registrazione avviata con successo per {username}!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
