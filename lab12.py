from adafruit_circuitplayground import cp
import time

morse_code = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}

def display_morse_code(morse_code_string, unit_length=0.2, color=(0, 255, 0)):
    for symbol in morse_code_string:
        if symbol == '.':
            cp.pixels.fill(color) 
            time.sleep(unit_length) 
            cp.pixels.fill((0, 0, 0))
            time.sleep(unit_length) 
        elif symbol == '-':
            cp.pixels.fill(color) 
            time.sleep(unit_length * 3) 
            cp.pixels.fill((0, 0, 0))
            time.sleep(unit_length)
        elif symbol == ' ':
            time.sleep(unit_length * 3)

def filter_sentence(sentence):
    sentence = sentence.lower()
    return ''.join([char for char in sentence if char.islower() or char.isdigit() or char == ' '])

def text_to_morse(text):
    morse = []
    words = text.split()
    for word in words:
        morse_word = []
        for char in word:
            if char in morse_code:
                morse_word.append(morse_code[char])
        morse.append(' '.join(morse_word))
    return ' '.join(morse)

def main():
    try:
        unit_length = float(input("Enter the unit length: "))
        red = int(input("Enter red value for color (0-255): "))
        green = int(input("Enter green value for color (0-255): "))
        blue = int(input("Enter blue value for color (0-255): "))
        if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
            raise ValueError("Color values must be between 0 and 255.")
        color = (red, green, blue)

        sentence = input("Enter a sentence: ")
        filtered_sentence = filter_sentence(sentence)
        morse_output = text_to_morse(filtered_sentence)

        print("Filtered Sentence:", filtered_sentence)
        print("Morse Code:", morse_output)
        display_morse_code(morse_output, unit_length, color)
    except ValueError as e:
        print("Error:", e)

main()
