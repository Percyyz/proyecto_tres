# OPERADOR MORSA
Para implementar una traducción de texto a código Morse en Python, no necesitarías un "operador Morza" específico, sino más bien una función o un diccionario que asigne cada letra, número o símbolo a su equivalente en código Morse.
>EJEMPLO
```python
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', 
    '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', 
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}

def to_morse(text):
    morse = []
    for char in text.upper():
        if char in morse_code:
            morse.append(morse_code[char])
        else:
            morse.append(' ')
    return ' '.join(morse)

# Ejemplo de uso:
texto = "HELLO WORLD"
codigo_morse = to_morse(texto)
print(codigo_morse)
```
