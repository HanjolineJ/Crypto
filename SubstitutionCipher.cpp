#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
using namespace std;


//string alphabet = "abcdefghijklmnopqrstuvwxyz";
//string key = "qwertyuiopasdfghjklzxcvbnm";

string encrypt(string text, int a, int b){
string result;
for(char c : text){
int x = c - 'a';
int y = (a * x + b) % 26;
result = result + char( 'a' + y);
}
return result;
}

/*
string encrypt(string text, int shift){
string result;
for(char c : text){
int pos = ( c - 'a' + shift) % 26;
result = result + char( 'a' + pos);
}
return result;
}
*/
/*
string decrypt(string text, int shift){
string result;
int aInv = modInverse(a,26)
if(aInv == -1){
cout << "Error: a has no modular inverse mod 26." << endl;
return "";
}
for(char c : text){
int y = c - 'a';
int x = aInv * (y - b + 26)
//int pos = (c - 'a' - shift +26) % 26; 
result = result + char ('a' + pos);
}
return result;
} 
*/

/*
int main(){
string plaintext;
int key;
cout << "Enter the message: " ;
cin >> plaintext;

cout << "Enter the key: " ;
cin >> key;

string ciphertext = encrypt(plaintext, key);
cout << "Encerypted: " << ciphertext << endl;

string decryptedtext = decrypt(ciphertext, key);
cout << "Decrypted: " << decryptedtext << endl;
return 0;
}

*/

int main(){
string plaintext;
iint a, b;
cout << "Enter the message: ";
cin >> plaintext;

cout << "Enter the key a (coprime with 26): " ;
cin >> a;

cout << "Enter the key b: ";
cin >> b;

cout << "GCD (a,26): " <<  gcd(a,26) << endl;

if(gcd(a,26) != 1){
cout << "Include key a. Must be coprime with 26" << endl;
return 1;
}
/*
string ciphertext = encrypt(plaintext, a b);
cout << "Encrypted: " << ciphertext << endl;

string decryptedtext = decrypt(ciphertext, key);
cout << "Decrypted: " decryptedtext << endl;
*/
