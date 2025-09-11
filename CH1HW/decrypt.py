import string
from collections import Counter
import re

def clean_text(text):
    """All characters convert to lowercase"""
    return re.sub(r'[^a-zA-Z]', '', text.lower())

def frequency_analysis(text):
    """Calculate frequency of each letter in the text"""
    clean = clean_text(text)
    total_letters = len(clean)
    
    if total_letters == 0:
        return {}
    
    # Count frequency of each letter
    letter_counts = Counter(clean)
    
    # Calculate percentages
    frequencies = {}
    for letter in string.ascii_lowercase:
        count = letter_counts.get(letter, 0)
        frequencies[letter] = (count, (count / total_letters) * 100)
    
    return frequencies

def display_frequencies(frequencies, title="Letter Frequencies"):
    """Display frequency analysis in bar format"""
    print(f"\n{title}")
    print("Letter | Count | Percentage")
    
    # Sort by frequency (descending)
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1][0], reverse=True)
    
    for letter, (count, percentage) in sorted_freq:
        if count > 0:  # Only show letters that appear
            print(f"  {letter.upper()}    |  {count:3d}  |  {percentage:6.2f}%")

def create_substitution_key(cipher_freq_order, english_freq_order):
    """Create substitution key mapping cipher letters to English letters"""
    key = {}
    for i, cipher_letter in enumerate(cipher_freq_order):
        if i < len(english_freq_order):
            key[cipher_letter] = english_freq_order[i]
    return key

def apply_substitution(ciphertext, substitution_key):
    """Apply substitution key to decode the ciphertext"""
    result = ""
    for char in ciphertext.lower():
        if char in substitution_key:
            result += substitution_key[char]
        elif char.isalpha():
            result += char  # Keep unmapped letters as is
        else:
            result += char  # Keep spaces and punctuation
    return result


def main():
    # The ciphertext image
    ciphertext = """
    lrvmnlr bpr sumvbwvr jx bpr lmlwv yjerykbi jx qmbm wi
    bpr xjvni mkd ymibryf jx irhx wi bpr riirvkr jx
    ymbinlmtmipw yfn qmumbr dj w ipmhh buf bj rhnvwdmbr bpr
    yjerykbi jx bpr qmbm mvvjudwko bj yf wkbrusurbmjwjk
    lmird jk xjubf trmui jx ibndf
    wb wi kjb nk rmlf bmlq bj rashmwk rmvp yjerykb mkd whi
    iwokvmwxmkvr mkd ijyr ynib urymwk nkrashmwkrd bj owrr
    vjyshrtr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
    wkiswrd bj invp nk rabrkb bpmb pr vjnhd urmvp bpr ibmtr
    jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgko i jnkdhrrii
    ijnkd mkd ipmsrhrll ipmsrr w dj kjb drry yfirhx bpr xwrnn
    mnbbjuwbj lnb yf rasruwrkvr cwbp qmbm pmi hrxb kj djnib
    bpmb bpr xjhhjcwko wi bpr sujsru msshwvmmbwjk mkd
    wkbrusurbmbjwjk w jxxru yf bprjuwri wk bpr pjsr bpmb bpr
    riirvkr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
    """
    secondtext = """xultpaajcxitltlxaarpjhtlwtgxktghidhlpxciwtvgtpilpit"""

    # Common English letter frequencies (approximate)
    english_freq_order = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u', 
                         'c', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']
    
    print("SUBSTITUTION CIPHER")
    
    # Perform frequency analysis
    frequencies = frequency_analysis(ciphertext)
    frequencies2 = frequency_analysis(secondtext)
    display_frequencies(frequencies, "Ciphertext Letter Frequencies")
    display_frequencies(frequencies2, "Second Text Letter Frequencies")

    # Get cipher letters ordered by frequency
    cipher_freq_order = [letter for letter, (count, _) in 
                        sorted(frequencies.items(), key=lambda x: x[1][0], reverse=True) 
                        if count > 0]
    
    print(f"\nCipher letters by frequency: {' '.join(cipher_freq_order).upper()}")
    print(f"English letters by frequency: {' '.join(english_freq_order).upper()}")
    
    # Create automatic substitution key based on frequency matching
    auto_key = create_substitution_key(cipher_freq_order, english_freq_order)
    
    print(f"\nAutomatic substitution key (cipher -> english):")
    for cipher, plain in sorted(auto_key.items()):
        print(f"  {cipher.upper()} -> {plain.upper()}")
    
    # Automatic substitution
    decoded_auto = apply_substitution(ciphertext, auto_key)
    print(f"\nAutomatic decryption attempt:")
    print("-" * 40)
    print(decoded_auto[:1000000] + "..." if len(decoded_auto) > 2 else decoded_auto)

    decoded_auto2 = apply_substitution(secondtext, auto_key)
    print(f"\nAutomatic decryption attempt for second text:")
    print("-" * 40)
    print(decoded_auto2[:1000000] + "..." if len(decoded_auto2) > 2 else decoded_auto2)

    
    # Based on notes, suggested mapping
    print(f"\nBased on  notes, suggested mappings:")
    suggested_key = {
        'b': 't', 'p': 'h', 'r': 'e', 'j': 'o', 'x': 'f',
        'w': 'i', 'm': 'a', 'k': 'n', 'd': 'd', 'q': 'c',
        'l': 'l', 'v': 'r', 'n': 'u', 'y': 'm', 'u': 'p',
        'i': 's', 'h': 'w', 'g': 'g', 't': 'y', 'o': 'v',
        's': 'b', 'f': 'k', 'c': 'q', 'e': 'x', 'z': 'z'
    }
    
    decoded_suggested = apply_substitution(ciphertext, suggested_key)
    #print("Suggested decryption:")
    #print("-" * 40)
    print(decoded_suggested[:100000] + "..." if len(decoded_suggested) > 3 else decoded_suggested)
    decoded_suggested2 = apply_substitution(secondtext, suggested_key)
    #print("Suggested decryption for second text:")  
    #print("-" * 40)
    print(decoded_suggested2[:100000] + "..." if len(decoded_suggested2) > 3 else decoded_suggested2)

if __name__ == "__main__":
    main()

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts an affine cipher.
    x = a_inv * (y - b) mod 26
    """
    # 1. Find modular multiplicative inverse of 'a'
    # a_inv must be a number such that (a * a_inv) % 26 == 
    # 7 * 15 = 105. 105 % 26 = 1. So a_inv = 15.
    a_inv = -1
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inv = i
            break
    
    if a_inv == -1:
        return "Error: The key 'a' has no modular inverse."

    plaintext = ""
    for char in ciphertext:
        if 'a' <= char <= 'z':
            y = ord(char) - ord('a')
            x = (a_inv * (y - b)) % 26
            if x < 0:
                x += 26
            plaintext += chr(x + ord('a'))
        else:
            plaintext += char
            
    return plaintext

def solve_affine_cipher():
    print("SOLVING AFFINE CIPHER")

    # Given key
    a = 7
    b = 22
    
    # Text to decrypt
    ciphertext = "falszztysyjyjkywjrztyjztyynaryjkywswarztyegyyj"
    
    print(f"Key a = {a}, b = {b}")
    print(f"Ciphertext: {ciphertext}")
    
    # Decrypt the text
    decrypted_text = affine_decrypt(ciphertext.replace(" ", ""), a, b)
    
    print(f"\nDecrypted Plaintext: {decrypted_text}")
    
    # Answer Who wrote the line?
    # The decrypted text is a famous quote.
    quote_parts = decrypted_text.split()
    formatted_quote = " ".join(quote_parts)
    print("\nFormatted Plaintext: " + formatted_quote.capitalize())

    print("\nWho wrote the line?")
    print("The line " + formatted_quote.capitalize() + " First the sentence and then the evidence as said the queen")
    print("This quote from Lewis Carroll's children's story Alice's Adventures in Wonderland.")

if __name__ == "__main__":
    main()
    solve_affine_cipher() # Call the new function at the end