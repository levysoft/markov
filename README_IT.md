# Markov Text Generator

<p align="center">
  <img src="logo.png" alt="Markov Text Generator">
</p>

## Catena di Markov per la Generazione di Nonsense Leggibili
Markov è un generatore di testo che utilizza una semplice catena di Markov per produrre testo leggibile ma privo di significato.
Questa tecnica, sebbene generi prosa che non ha molto valore letterario, è sorprendentemente utile per prevedere la prossima parola, simile ai suggerimenti della tastiera del telefono.

## Ispirazione
Questo progetto è stato ispirato dall'articolo "_Understanding Markov Chains_" di Ben Hoyt (https://benhoyt.com/writings/markov-chain/) e dal Capitolo 3 del libro "_The Practice of Programming_" di Kernighan and Pike (https://www.cs.princeton.edu/~bwk/tpop.webpage/). In particolare, l'articolo di Hoyt fornisce una spiegazione chiara dell'algoritmo e delle sue applicazioni, che vanno oltre la semplice generazione di testo.
Successivamente mi sono ispirato all'articolo "_Markov Chains are the Original Language Models_" di Elijah Potter (https://elijahpotter.dev/articles/markov_chains_are_the_original_language_models) per creare anche una versione interattiva.


## Algoritmo
L'algoritmo inizia con un testo di input da cui generare l'output. Per ogni coppia di parole nel testo di input, registra una lista delle possibili parole che possono seguire la coppia. Una volta costruita questa struttura dati, è possibile generare output di qualsiasi lunghezza. Si inizia con una coppia di parole presente nell'input e si sceglie casualmente una delle possibili terze parole. Si procede poi spostandosi di parola in parola.

## Esempio
Per illustrare, utilizziamo un input piccolo come gli ultimi cinque dei Dieci Comandamenti dalla Bibbia del Re Giacomo. La struttura di "terze parole possibili" per alcune entrate iniziali sarebbe:

- shalt not: kill. | commit | steal. | bear | covet | covet
- Thou shalt: not | not | not | not | not

E così via. L'output generato rifletterà la struttura e il "sapore" del testo di input, aggiungendo un tocco di originalità.

## Implementazione in Python
Il codice è conciso e leggibile, composto da meno di 25 linee. Questo codice prevede che il numero di parole venga passato come argomento da riga di comando e che il testo di input venga fornito su stdin.

## Riferimenti per i File di Training
È possibile usare vari testi liberamente accessibili in formato txt come input per la generazione di contenuti la catena di Markov. Di seguito, i riferimenti ai testi utilizzati:

- Messaggio di Fine Anno del Presidente della Repubblica Sergio Mattarella (italiano): [https://www.quirinale.it/elementi/103914](https://www.quirinale.it/elementi/103914) (qui trovate l'archivio completo (italiano): [https://www.quirinale.it/ricerca/Discorsi](https://www.quirinale.it/ricerca/Discorsi))
- Le avventure d'Alice nel paese delle meraviglie di Lewis Carroll (italiano): [https://www.gutenberg.org/ebooks/28371](https://www.gutenberg.org/ebooks/28371)
- Le avventure d'Alice nel paese delle meraviglie di Lewis Carroll (inglese): [https://www.gutenberg.org/ebooks/19033](https://www.gutenberg.org/ebooks/19033)
- Discorso di John Fitzgerald Kennedy per l'accettazione della nomina a presidente dal Partito Democratico (inglese): [https://www.jfklibrary.org/learn/about-jfk/historic-speeches/acceptance-of-democratic-nomination-for-president](https://www.jfklibrary.org/learn/about-jfk/historic-speeches/acceptance-of-democratic-nomination-for-president)

## Esecuzione
Per eseguire lo script, utilizza il seguente comando:

```bash
python3 markov.py <numero_parole> <file_testo>
```
Dove `<numero_parole>` è il numero di parole che vuoi generare e `<file_testo>` è il percorso al file di testo di input.

## Test markov.py

```bash
python3 markov.py 100 ./training-texts/Alice.txt

Bruco con disprezzo. "Chi siete _voi_?" E ciò li ricondusse da capo al
principio della conversazione. Alice rispose con un cavallo di
vetturale, così per alimentare la conversazione. "Eh sì," rispose la
cuoca. "Di melazzo," soggiunse una voce rabbiosa--quella del
Coniglio:--"Gianni! Gianni! Dove sei?" E rispose una voce sonnolenta
dietro ad un usciere, "Recatemi la lista de' cantanti. "Potete
andare," disse il Bruco pipò senza dir nulla sullo sbaglio che il
rimaner col Grifone non l'ha mai imparata." "Non ebbi tempo," rispose
il Ghiro, "e si chiamavano Elce, Clelia e Tilla; e dimoravano nel
fondo del pozzo?" Il Ghiro scosse il capo;
```

```bash
python3 markov.py 100 ./training-texts/Mattarella.txt
  
Coltivarne la cultura nel sentimento delle nuove generazioni. Di
fronte alle quali si presentano oggi, e nel loro possibile avvenire,
brutalità che pensavamo, ormai, scomparse; oltre che condannate dalla
storia. La guerra non nasce da sola. Non basterebbe neppure la spinta
di tante armi, che ne sono lo strumento di morte. Così diffuse. Sempre
più letali. Fonte di enormi guadagni. Nasce da quel che c’è nell’animo
degli uomini. Dalla mentalità che si autoalimenta, sta generando un
progresso inarrestabile. Destinato a modificare profondamente le
nostre abitudini professionali, sociali, relazionali. Ci troviamo nel
mezzo di quello che verrà ricordato come il grande balzo storico
```

# Markov Interactive Script
Ho pensato di creare lo script Python markov-interactive.py per implementare una catena di Markov in modo che generasse testo in modo interattivo, permettendo all'utente di scegliere la parola successiva basata su percentuali calcolate dalla frequenza di comparsa nel testo di input. 

L'idea è di esplorare come le sequenze di parole (o "stati") si susseguono in un testo fornito, offrendo un'esperienza diretta nella generazione di testo basata su probabilità e consentendo agli utenti di influenzare direttamente il percorso della generazione del testo scegliendo tra le parole successive proposte.
Ciò, implicitamente, permetterà di esplorare la varietà linguistica e le potenziali direzioni narrative che emergono dall'utilizzo di diversi testi di input.

## Funzionamento
Lo script lavora in due fasi principali:

1. **Calcolo delle Percentuali:** Per ogni coppia di parole nel testo (`prefix`), calcola le percentuali per ogni possibile parola successiva. Questo passaggio si basa sul numero di volte che ogni parola segue direttamente la coppia data.

2. **Selezione Interattiva:** Presenta all'utente una lista numerata di parole possibili con le relative percentuali. L'utente seleziona il numero corrispondente alla parola desiderata per costruire progressivamente una nuova sequenza di testo.

## Esecuzione
Per eseguire lo script, utilizza il seguente comando:

```bash
python3 markov-interactive.py <numero_parole> <file_testo>
```

Dove `<numero_parole>` è il numero di parole che vuoi generare e `<file_testo>` è il percorso al file di testo di input.

## Test markov-interactive.py

```bash
python3 markov-interactive.py 100 ./training-texts/Alice.txt

--------------------------------------------------
Testo corrente:
Alice afferrò
--------------------------------------------------

Opzioni per 'Alice afferrò':
1. il: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
Alice afferrò il
--------------------------------------------------

Opzioni per 'afferrò il':
1. bimbo: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo
--------------------------------------------------

Opzioni per 'il bimbo':
1. guaiva: 20.00%
2. su: 20.00%
3. in: 20.00%
4. ma: 20.00%
5. porcellino: 20.00%
Scegli il numero della prossima parola: 2

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su
--------------------------------------------------

Opzioni per 'bimbo su':
1. e: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su e
--------------------------------------------------

Opzioni per 'su e':
1. giù: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su e giù
--------------------------------------------------

Opzioni per 'e giù':
1. provando: 50.00%
2. con: 50.00%
Scegli il numero della prossima parola: 2

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su e giù con
--------------------------------------------------

Opzioni per 'giù con':
1. molta: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su e giù con molta
--------------------------------------------------

Opzioni per 'con molta':
1. allegrezza: 5.26%
2. civiltà:: 5.26%
3. gravità: 5.26%
4. avvedutezza: 5.26%
5. violenza,: 5.26%
6. ansietà: 5.26%
7. deferenza.: 5.26%
8. curiosità,: 5.26%
9. delicatezza.: 5.26%
10. premura.: 5.26%
11. delicatezza:: 5.26%
12. garbatezza,: 10.53%
13. curiosità.: 5.26%
14. premura: 10.53%
15. sollecitudine,: 5.26%
16. enfasi,: 5.26%
17. delicatezza: 5.26%
Scegli il numero della prossima parola: 17

--------------------------------------------------
Testo corrente:
Alice afferrò il bimbo su e giù con molta delicatezza
--------------------------------------------------
```

## Note sulla Generazione di Testo
- **Testi con Limitata Varietà di Transizioni:** Se il testo di input presenta una limitata varietà di sequenze di parole, potresti notare che le percentuali tendono spesso al 100% per la parola successiva, indicando una sola opzione possibile.

- **Uso di Testi Vari e Ricchi:** Utilizzando testi con maggiore varietà linguistica (come "Alice nel Paese delle Meraviglie"), lo script offre una gamma più ampia di scelte, rendendo la generazione di testo più dinamica e imprevedibile.

Questo comportamento rispecchia la natura delle catene di Markov, che si basano esclusivamente sulla frequenza delle parole senza considerare il contesto più ampio o la coerenza grammaticale.

## Conclusione
L'algoritmo di catena di Markov, nonostante la sua semplicità, è un'introduzione pratica al concetto di catene di Markov che rivela come una struttura dati semplice e un generatore di numeri casuali possano produrre output affascinanti, semplicemente "remixando" testi esistenti in modi nuovi e creativi.

## Licenza
Questo progetto è liberamente ispirato e basato su concetti esposti nell'articolo di Ben Hoyt e nel libro di Kernighan e Pike. Sei libero di utilizzare, modificare e distribuire il codice come preferisci.

