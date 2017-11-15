# Python Ciphers

### Reverse Cipher

This cipher simply takes the input message and reverses it, including all punctuation and non-letter symbols.

### Caesar Cipher

This cipher takes a message, a key, and a mode (encrypt or decrypt), as well as a dictionary of symbols (letters in this example - other symbols/punctuation can be added) to encrypt and decrypt a message.

* When the message is to be encrypted, the script runs through each letter/symbol in the original message, and encrypts it based on the key used for the encryption, which is added to that letter/symbol's indexed value. Overflow is handled by "looping back" toward the beginning of the dictionary.

* When the message is to be decrypted, the script runs through each letter/symbol in the original message, and decrypts it based on the key used for the decryption, which is subtracted from that letter/symbol's indexed value. Overflow is handled by "looping forward" toward the end of the dictionary.