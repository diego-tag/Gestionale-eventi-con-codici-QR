# Progetto Ingegneria del Software

Benvenuti nel repository del progetto di Ingegneria del Software. Questa repo include il codice sorgente Python, i diagrammi UML e la relazione in latex del progetto.

## Struttura del repository

- **root**  
  Si trova `Gestionale eventi QR.eapx`, il file necessario per i diagrammi UML e un PDF dove è illustrata la struttura consigliata per la relazione (tesina).

- **relazione**  
  Contiene tutti i file e i pacchetti necessari per la compilazione della relazione in LaTeX. Vi è disponibile anche la relazione in formato `.pdf`.

- **app**  
  Contiene l'intero codice sorgente del software gestionale implementato in Python.
  
## Requisiti

- **Python 3.x**  
  Assicurarsi di avere installato Python di versione 3 o successiva.

- **Enterprise Architect**  
  Per aprire e modificare il file `.eapx` che contiene i diagrammi UML, è richiesto Enterprise Architect o un software compatibile.

- **LaTeX**  
  Per la compilazione della relazione, è necessario avere un ambiente LaTeX installato (ad esempio, TeX Live o MikTeX) oppure un IDE (TeXstudio, VS code o altri).

## Istruzioni per eseguire il software

1. Clonare il repository:
   ```bash
   git clone https://github.com/diego-tag/Gestionale-eventi-con-codici-QR.git
   ```
2. Spostarsi nella cartella del software:
   ```bash
   cd app
   ```
3. Eseguire il software con Python:
   ```bash
   python main.py
   ```

## Generazione della documentazione

- **Diagrammi UML**:  
  Aprire il file `.eapx` situato nella root con Enterprise Architect per visualizzare e modificare i diagrammi UML.

- **Relazione in LaTeX**:  
  Navigare nella cartella `relazione` e compilare il documento LaTeX (con pdflatex o simili):
  ```bash
  pdflatex relazione.tex
  ```
  *Eventuali ulteriori dipendenze o pacchetti LaTeX dovranno essere gestiti a seconda della configurazione del documento.*