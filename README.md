# Markov Text Generator

<p align="center">
  <img src="logo.png" alt="Markov Text Generator">
</p>

## Markov Chain for Generating Readable Nonsense
Markov is a text generator that uses a simple Markov chain to produce readable but nonsensical text. Although this technique generates prose of little literary value, it's surprisingly useful for predicting the next word, similar to phone keyboard suggestions.

## Inspiration
This project was inspired by Ben Hoyt's article "_Understanding Markov Chains_"(https://benhoyt.com/writings/markov-chain/) and Chapter 3 of "_The Practice of Programming_" by Kernighan and Pike (https://www.cs.princeton.edu/~bwk/tpop.webpage/). Hoyt's article, in particular, provides a clear explanation of the algorithm and its applications beyond mere text generation.
Subsequently, I was inspired by the article "_Markov Chains are the Original Language Models_" by Elijah Potter (https://elijahpotter.dev/articles/markov_chains_are_the_original_language_models) to also create an interactive version.

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

## Execution
To run the script, use the following command:

```bash
python3 markov.py <number_of_words> <text_file>
```

Where <number_of_words> is the number of words you want to generate and <text_file> is the path to the input text file.

## Test markov.py

```bash
python3 markov.py 100 Alice_Adventures_in_Wonderland

Caterpillar seemed to be afraid of it. "No room! No room!" they cried
out when they liked and left off quarreling with the other; the only
difficulty was that she had gone through that day. "You're looking for
eggs, as it turned a corner, "Oh, my ears and whiskers, how late it's
getting!" She was delighted to find herself talking familiarly with
them, as if she had put on one knee. "I'm a poor man, Your Majesty,"
said Alice to find my way into a cucumber-frame or something of that
is--'Oh, 'tis love, 'tis love that makes you forget to talk." "The```

```bash
python3 markov.py 100 Kennedy.txt
  
Richard Nixon did not measure to the safe mediocrity of the 1960's--a
frontier of the New Frontier is here, whether we seek it or not.
Beyond that frontier are the uncharted areas of science and space,
unsolved problems of peace and war, unconquered pockets of ignorance
and prejudice, unanswered questions of poverty and surplus. It would
be easier to shrink back from that frontier, to look to the Scriptural
call: "Be strong and free, to overcome its hazards and its hardships,
to conquer the enemies that threatened from without and within. Today
some would say that those struggles are all over--that all
```
# Markov Interactive Script
I decided to create the Python script markov-interactive.py to implement a Markov chain in a way that it generates text interactively, allowing the user to choose the next word based on percentages calculated from the frequency of appearance in the input text.

The idea is to explore how word sequences (or "states") follow each other in a provided text, offering a direct experience in text generation based on probabilities and allowing users to directly influence the path of text generation by choosing from the proposed next words.
This implicitly will enable exploring linguistic variety and potential narrative directions that emerge from using different input texts.

## How It Works
The script operates in two main phases:

1. **Percentage Calculation:** For each pair of words in the text (`prefix`), it calculates the percentages for each possible following word. This step is based on the number of times each word directly follows the given pair.

2. **Interactive Selection:** Presents the user with a numbered list of possible words along with their percentages. The user selects the number corresponding to the desired word to progressively construct a new text sequence.

## Execution
To run the script, use the following command:

```bash
python3 markov-interactive.py <number_of_words> <text_file>
```

Where `<number_of_words>` is the number of words you want to generate and `<text_file>` is the path to the input text file.

## Test markov-interactive.py

```bash
python3 markov-interactive.py 100 Alice_Adventures_in_Wonderland.txt

--------------------------------------------------
Testo corrente:
White Rabbit,
--------------------------------------------------

Opzioni per 'White Rabbit,':
1. trotting: 20.00%
2. who: 40.00%
3. with: 20.00%
4. jumping: 20.00%
Scegli il numero della prossima parola: 4

--------------------------------------------------
Testo corrente:
White Rabbit, jumping
--------------------------------------------------

Opzioni per 'Rabbit, jumping':
1. up: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
White Rabbit, jumping up
--------------------------------------------------

Opzioni per 'jumping up':
1. and: 50.00%
2. in: 50.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
White Rabbit, jumping up and
--------------------------------------------------

Opzioni per 'up and':
1. picking: 11.11%
2. went: 11.11%
3. walking: 11.11%
4. said: 11.11%
5. down: 11.11%
6. walked: 11.11%
7. stand: 11.11%
8. there: 11.11%
9. ran: 11.11%
Scegli il numero della prossima parola: 3

--------------------------------------------------
Testo corrente:
White Rabbit, jumping up and walking
--------------------------------------------------

Opzioni per 'and walking':
1. away.: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
White Rabbit, jumping up and walking away.
--------------------------------------------------

Opzioni per 'walking away.':
1. "Please: 100.00%
Scegli il numero della prossima parola: 1

--------------------------------------------------
Testo corrente:
White Rabbit, jumping up and walking away. "Please
--------------------------------------------------

Opzioni per 'away. "Please':
1. come: 100.00%
```
## Notes on Text Generation
- **Texts with Limited Variety of Transitions:** If the input text has a limited variety of word sequences, you might notice that the percentages often tend towards 100% for the next word, indicating only one possible option.

- **Using Diverse and Rich Texts:** By using texts with greater linguistic variety (such as "Alice in Wonderland"), the script offers a wider range of choices, making text generation more dynamic and unpredictable.

This behavior reflects the nature of Markov chains, which rely solely on the frequency of words without considering broader context or grammatical coherence.

## Conclusion
Despite its simplicity, the Markov chain algorithm reveals how a simple data structure and a random number generator can produce fascinating output. This project is an example of how elegant design choices can simplify code and enhance output.

## License
This project is freely inspired by and based on concepts presented in Ben Hoyt's article and Kernighan and Pike's book. You are free to use, modify, and distribute the code as you wish.
