import collections
import random
import sys
import textwrap

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 script.py <numero_parole> <file_testo>")
        sys.exit(1)

    num_words = int(sys.argv[1])
    file_path = sys.argv[2]

    w1 = w2 = ''
    possibles = collections.defaultdict(list)

    # Legge il file per costruire la tabella delle parole possibili
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                possibles[w1, w2].append(word)
                w1, w2 = w2, word

    # Evita liste di possibili vuote alla fine dell'input
    possibles[w1, w2].append('')
    possibles[w2, ''].append('')

    # Genera output casuale partendo da un prefisso maiuscolo casuale
    w1, w2 = random.choice([k for k in possibles if k[0][:1].isupper()])
    output = [w1, w2]
    for _ in range(num_words):
        word = random.choice(possibles[w1, w2])
        output.append(word)
        w1, w2 = w2, word

    # Stampa l'output formattato a 70 colonne
    print(textwrap.fill(' '.join(output)))

if __name__ == "__main__":
    main()
