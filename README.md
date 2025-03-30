# Progetto Ingegneria del Software

Benvenuti nel repository del progetto di Ingegneria del Software. Questa repo include il codice sorgente Python, i diagrammi UML e la relazione in latex del progetto.

## Struttura del Repository

- **root**  
  In questa cartella si trova il file `.eap` (Enterprise Architect Project) necessario per i diagrammi UML.

- **relazione**  
  Contiene tutti i file e i pacchetti necessari per la compilazione della relazione in LaTeX.

- **app**  
  Contiene l'intero codice sorgente del software gestionale implementato in Python.
  
## Requisiti

- **Python 3.x**  
  Assicurarsi di avere installato Python di versione 3 o successiva.

- **Enterprise Architect**  
  Per aprire e modificare il file `.eap` che contiene i diagrammi UML, è richiesto Enterprise Architect o un software compatibile.

- **LaTeX**  
  Per la compilazione della relazione, è necessario avere un ambiente LaTeX installato (ad esempio, TeX Live o MikTeX) oppure un IDE (TeXstudio, VS code o altri).

## Istruzioni per l'Esecuzione del programma

1. Clonare il repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   ```
2. Spostarsi nella cartella del progetto:
   ```bash
   cd gestionale-python
   ```
3. Eseguire il software:
   ```bash
   python app/main.py
   ```

## Generazione della Documentazione

- **Diagrammi UML**:  
  Aprire il file `.eap` situato nella root con Enterprise Architect per visualizzare e modificare i diagrammi UML.

- **Relazione in LaTeX**:  
  Navigare nella cartella `relazione` e compilare il documento LaTeX:
  ```bash
  pdflatex relazione.tex
  ```
  *Eventuali ulteriori dipendenze o pacchetti LaTeX dovranno essere gestiti a seconda della configurazione del documento.*