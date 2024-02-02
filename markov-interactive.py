import collections
import random
import sys
import textwrap

def calculate_percentages(possibles, prefix):
    words = possibles[prefix]
    total_count = len(words)
    word_counts = collections.Counter(words)
    percentages = {word: count / total_count * 100 for word, count in word_counts.items()}
    return percentages

def print_current_text(output):
    # Aggiunta di separatori per una migliore leggibilità dell'output
    print("\n" + "-"*50)
    print("Testo corrente:")
    print(textwrap.fill(' '.join(output), width=70))
    print("-"*50 + "\n")

def main():
    try:
        if len(sys.argv) < 3:
            print("Uso: python3 markov-interactive.py <numero_parole> <file_testo>")
            sys.exit(1)
    
        num_words = int(sys.argv[1])
        file_path = sys.argv[2]
    
        w1 = w2 = ''
        possibles = collections.defaultdict(list)
        with open(file_path, 'r') as file:
            for line in file:
                for word in line.split():
                    possibles[w1, w2].append(word)
                    w1, w2 = w2, word
    
        # Evita liste di possibili vuote alla fine dell'input
        possibles[w1, w2].append('')
        possibles[w2, ''].append('')
    
        # Inizia con un prefisso casuale maiuscolo
        w1, w2 = random.choice([k for k in possibles if k[0][:1].isupper()])
        output = [w1, w2]
        for _ in range(num_words):
            percentages = calculate_percentages(possibles, (w1, w2))
    
            print_current_text(output)

            #print(f"Debug - Possibili parole dopo '{w1} {w2}': {possibles[w1, w2]}")
            
            options = list(percentages.items())
            print(f"Opzioni per '{w1} {w2}':")
            for i, (word, percentage) in enumerate(options, start=1):
                print(f"{i}. {word}: {percentage:.2f}%")
    
            while True:
                try:
                    choice = int(input("Scegli il numero della prossima parola: ")) - 1
                    if choice < 0 or choice >= len(options):
                        print("Scelta non valida. Riprova.")
                        continue
                    break
                except ValueError:
                    print("Per favore, inserisci un numero valido.")
    
            next_word = options[choice][0]
            output.append(next_word)
            w1, w2 = w2, next_word
    
        # Stampa l'output finale del testo completo
        print_current_text(output)

    except KeyboardInterrupt:
        print("\nProgramma interrotto. Arrivederci!")
        sys.exit(0)

if __name__ == "__main__":
    main()
