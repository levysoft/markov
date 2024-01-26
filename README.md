# Markov Text Generator

<p align="center">
  <img src="logo.png" alt="Markov Text Generator">
</p>

## Markov Chain for Generating Readable Nonsense
Markov is a text generator that uses a simple Markov chain to produce readable but nonsensical text. Although this technique generates prose of little literary value, it's surprisingly useful for predicting the next word, similar to phone keyboard suggestions.

## Inspiration
This project was inspired by Ben Hoyt's article "_Understanding Markov Chains_"(https://benhoyt.com/writings/markov-chain/) and Chapter 3 of "_The Practice of Programming_" by Kernighan and Pike (https://www.cs.princeton.edu/~bwk/tpop.webpage/). Hoyt's article, in particular, provides a clear explanation of the algorithm and its applications beyond mere text generation.

## Algorithm
The algorithm starts with an input text from which to generate output. For each pair of words in the input text, it records a list of possible words that can follow the pair. Once this data structure is built, you can generate output of any length. Start with any pair of words that occurs in the input and randomly choose one of the possible third words. Then move along, using the second word in the pair and the newly generated word as the next pair.

## Example
To illustrate, let's use a small input like the last five of the Ten Commandments from the King James Bible. The "possible third words" structure for some initial entries would be:

- shalt not: kill. | commit | steal. | bear | covet | covet
- Thou shalt: not | not | not | not | not

And so on. The generated output will reflect the structure and "flavor" of the input text, adding a touch of originality.

## Python Implementation
The code is concise and readable, consisting of fewer than 25 lines. This code expects the number of words to be passed as a command-line argument and the input text to be provided on stdin.

## References for Training Files
You can use various freely accessible text files in txt format as input for Markov chain content generation. Below are the references to the texts used:

- New Year's Message from the President of the Republic Sergio Mattarella (mattarella.txt): [https://www.quirinale.it/elementi/103914](https://www.quirinale.it/elementi/103914) (complete archive available here: [https://www.quirinale.it/ricerca/Discorsi](https://www.quirinale.it/ricerca/Discorsi))
- Alice's Adventures in Wonderland by Lewis Carroll: [https://www.gutenberg.org/ebooks/28371](https://www.gutenberg.org/ebooks/28371)
- Alice's Adventures in Wonderland (Italian) by Lewis Carroll: [https://www.gutenberg.org/ebooks/19033](https://www.gutenberg.org/ebooks/19033)

## Test

```bash
python3 markov.py 100 < Alice.txt

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
python3 markov.py 100 < mattarella.txt
  
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

## Conclusion
Despite its simplicity, the Markov chain algorithm reveals how a simple data structure and a random number generator can produce fascinating output. This project is an example of how elegant design choices can simplify code and enhance output.

## License
This project is freely inspired by and based on concepts presented in Ben Hoyt's article and Kernighan and Pike's book. You are free to use, modify, and distribute the code as you wish.
