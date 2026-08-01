# 📱 Instagram Live Auto-Recorder (Tasker + Flask)

Uso Educativo: Questo progetto e il codice sorgente allegato sono stati creati a scopo puramente educativo e di ricerca, per dimostrare l'integrazione tra automazioni Android (Tasker), Webhook e server web Python (Flask).

Questo progetto è un'automazione che intercetta le notifiche delle dirette Instagram su uno smartphone Android (usando **Tasker**) e fa partire automaticamente la registrazione del video su un server remoto utilizzando **Flask** e **PyInstaLive**.

In breve: se un account che segui fa partire una diretta, il tuo telefono se ne accorge e dice al tuo server di iniziare a registrarla, inviandoti anche una notifica di conferma tramite IFTTT.

## 🚀 Architettura del Progetto

1.  **Tasker (Android):** Ascolta le notifiche di sistema in arrivo dall'app di Instagram. Quando identifica una notifica di una nuova diretta, estrapola il nome utente e fa una richiesta HTTP POST al server Flask.
2.  **Flask (Server Python):** Riceve il nome utente, pulisce l'input ed esegue in modo sicuro la libreria `PyInstaLive` per scaricare la diretta.
3.  **IFTTT (Opzionale):** Il server invia una richiesta webhook a IFTTT per notificarti che la registrazione è iniziata con successo.

## 🛠️ Prerequisiti

*   Un server Python (es. PythonAnywhere, Heroku, VPS) con Python 3.
*   L'app [Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm) installata sul tuo dispositivo Android.
*   Il pacchetto [PyInstaLive](https://github.com/dvingerh/PyInstaLive) installato e configurato sul server con un account Instagram valido.

## 📦 Installazione Server

1. Clona il repository:
   ```bash
   git clone [https://github.com/tuo-username/nome-repo.git](https://github.com/tuo-username/nome-repo.git)
   cd nome-repo
   ```

2. Installa le dipendenze per Flask e PyInstaLive:
   ```bash
   pip install Flask requests pyinstalive
   ```

3. (Opzionale) Configura la variabile d'ambiente per ricevere la notifica IFTTT:
   ```bash
   export IFTTT_WEBHOOK_KEY="la-tua-chiave-segreta"
   ```

4. Avvia l'applicazione:
   ```bash
   python app.py
   ```

## 📱 Configurazione Tasker (Android)

Per far comunicare lo smartphone con il server Flask, è necessario configurare Tasker utilizzando il plugin **AutoNotification** per intercettare gli avvisi di Instagram.

1.  **Creazione del Profilo:**
    *   In Tasker, crea un nuovo profilo basato su un evento di tipo **AutoNotification Intercept Event Behaviour**.
    *   Configura il plugin per reagire specificamente alle notifiche in arrivo dall'app di Instagram relative all'avvio di una nuova diretta.
    *   Collega questo profilo a una nuova attività (Task) nominandola `Notifica`.

2.  **Creazione dell'Attività (Task):**
    *   All'interno dell'attività `Notifica`, aggiungi un'azione di tipo **Richiesta HTTP**.
    *   Imposta il *Metodo* su **POST**.
    *   Nel campo *URL*, inserisci l'indirizzo del tuo server PythonAnywhere (ad esempio `https://chrissssss.py...`) seguito dall'endpoint corretto per il tuo script Flask.
    *   Nel corpo (Body) della richiesta, passa la variabile generata da AutoNotification che contiene il testo della notifica, in modo che il server possa estrarre il nome utente. (%antextbig)

## ⚠️ Disclaimer Legale e Responsabilità

> **Uso Educativo:** Questo progetto e il codice sorgente allegato sono stati creati a scopo puramente **educativo e di ricerca**, per dimostrare l'integrazione tra automazioni Android (Tasker), Webhook e server web Python (Flask).

> **Violazione dei Termini di Servizio (ToS):** L'utilizzo di script, bot o client non ufficiali per accedere, interagire o scaricare contenuti da Instagram costituisce una violazione diretta dei Termini di Servizio di Meta Platforms, Inc. L'utilizzo di questo codice con un account Instagram reale comporta un **alto rischio di ban permanente** dell'account stesso.

> **Copyright e Privacy:** La registrazione, il salvataggio e la potenziale ridistribuzione di video in diretta (Live) senza il consenso esplicito del creatore originale possono violare le leggi sul diritto d'autore (Copyright) e i regolamenti sulla privacy (come il GDPR). 

> **Esclusione di Responsabilità:** L'autore di questo repository **non si assume alcuna responsabilità** per eventuali conseguenze derivanti dall'utilizzo, proprio o improprio, di questo software. L'utente finale è l'unico responsabile delle proprie azioni e si impegna a rispettare le leggi vigenti e le policy delle piattaforme coinvolte. Utilizza questo strumento a tuo rischio e pericolo.

> Using this script may result in your account being suspended, use at your own risk.

## 🛡️ Sicurezza

Questo script è stato scritto prestando attenzione alla sicurezza:
* Non sono presenti chiavi API cablate (hardcoded) nel codice.
* L'esecuzione dei comandi di sistema per avviare PyInstaLive usa `subprocess.run` con il passaggio degli argomenti tramite lista. Questo previene in modo assoluto le vulnerabilità di **Command Injection**, impedendo che un utente malintenzionato possa inviare comandi bash tramite richieste web contraffatte.
