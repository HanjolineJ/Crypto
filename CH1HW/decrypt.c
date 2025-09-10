#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Finds the modular multiplicative inverse of 'a' under modulo 'm'
int mod_inverse(int a, int m) {
    for (int x = 1; x < m; x++) {
        if (((a % m) * (x % m)) % m == 1) {
            return x;
        }
    }
    return -1; // Inverse does not exist
}

// Decrypts the ciphertext using the key (a, b)
void decrypt(const char* ciphertext, int a, int b) {
    // First, find the modular inverse of 'a'
    int a_inv = mod_inverse(a, 26);
    if (a_inv == -1) {
        printf("Error: Key 'a'=%d is not valid.\n", a);
        return;
    }

    printf("--- Decrypted Message ---\n");
    // Loop through each character of the ciphertext
    for (int i = 0; i < strlen(ciphertext); i++) {
        char c = ciphertext[i];

        // Only decrypt lowercase letters
        if (islower(c)) {
            // Convert char to number (a=0, b=1, ...)
            int C = c - 'a';
            // Apply decryption formula: P = a_inv * (C - b) mod 26
            // We add 26 to handle potential negative numbers before the modulo.
            int P = (a_inv * (C - b + 26)) % 26;
            // Convert number back to char and print
            putchar(P + 'a');
        } else {
            // If not a letter, print it as is
            putchar(c);
        }
    }
    printf("\n");
}

int main() {
    // The correctly transcribed ciphertext from the textbook image
    const char* CIPHERTEXT = "lrvmnirbprsumvbwrvjxbprlmiwvyjeryrkbijxqmbmwibprxjynimkdymibrutjxirhxwibprriirkvrjxymbinlmtmipwutnqmbmrdjwi"
                             "pmhhbutbjrhnvvdmbrbpryjeryrkbijxbprqmbmmvvjudwkobjytwkbrusbmbwjklmirdjkxjubttrmuijxibndtwbwikjbmkrmitbmiqb"
                             "jrashmwkrmvpyjeryrkbmkdwbiiwokwxvmkvrmkdijyryniburymwknkrashmwkrdbjowermvjyshrbrrashmbwjkjkrcjnhdpmerbjlrfn"
                             "mhxwrdmkdwkiswurbjinvpmkrabrkbbpmbprvjnhdurmvpbprimbmrjxrkhwopbrkrdywkdvmscmlhrjxurvjokwgwkoijnkdhriiijnkdm"
                             "kdipmsrhriiipmsrwdjkjbdrryytirhxbprxwkmnmnbpjuwbtlnbytrasruwrkvrcwbpqmbmpmihrxbkjdjnlobpmbprxjhhjcwkowibpr"
                             "sujsrumsshwvmbwjkmkdwkbrusbmbwjkjwjxxruytbprjuwriwkbprpjsrbpmbprriirkvrjxjqwkmcmkqmumbrcwhhurymwkwkbmvb";

    // The correct key found via frequency analysis
    int key_a = 7;
    int key_b = 21;

    printf("Decrypting with key a=%d, b=%d...\n", key_a, key_b);

    decrypt(CIPHERTEXT, key_a, key_b);

    return 0;
}