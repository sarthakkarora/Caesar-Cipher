
# Caesar Cipher

<br>

![Screenshot 2024-04-26 at 6 50 59 PM](https://github.com/sarthakkarora/Caesar-Cipher/assets/130503783/71206e72-e17d-484f-8dd6-1e99a923b1ae)

<br>
The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the “shift” or “key”.

The Caesar Cipher technique is one of the earliest and simplest methods of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.

Thus to cipher a given text we need an integer value, known as a shift which indicates the number of positions each letter of the text has been moved down. The encryption can be represented using modular arithmetic by first transforming the letters into numbers, according to the scheme, A = 0, B = 1,…, Z = 25. Encryption of a letter by a shift n can be described mathematically as. For example, if the shift is 3, then the letter A would be replaced by the letter D, B would become E, C would become F, and so on. The alphabet is wrapped around so that after Z, it starts back at A.

![Screenshot 2024-04-29 at 11 16 49 PM](https://github.com/sarthakkarora/Caesar-Cipher/assets/130503783/2ba3fb5c-c2cf-4864-bab7-58e38a7fb303)

Here is an example of how to use the Caesar cipher to encrypt the message “HELLO” with a shift of 3:

1. Write down the plaintext message: HELLO
2. Choose a shift value. In this case, we will use a shift of 3.
3. Replace each letter in the plaintext message with the letter that is three positions to the right in the alphabet.
   - H becomes K (shift 3 from H)
   - E becomes H (shift 3 from E)
   - L becomes O (shift 3 from L)
   - L becomes O (shift 3 from L)
   - O becomes R (shift 3 from O)
4. The encrypted message is now “KHOOR”.

To decrypt the message, you simply need to shift each letter back by the same number of positions. In this case, you would shift each letter in “KHOOR” back by 3 positions to get the original message, “HELLO”.

## Encryption and Decryption Formulas

- Encryption Phase with shift \( n \): \( E_n(x) = (x + n) \mod 26 \)
- Decryption Phase with shift \( n \): \( D_n(x) = (x - n) \mod 26 \)

![Caesar Cipher](https://github.com/sarthakkarora/Caesar-Cipher/assets/130503783/c59d4c95-96cc-4e4d-bcd2-1e20b054317a)
