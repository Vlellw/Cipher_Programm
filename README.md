# Cipher App

This application provides a graphical user interface for encrypting and decrypting text using various cryptographic methods. Below is a description of each class and function in the code:

## Classes:

* **Dialog**:

    This class represents the main window of the application.
    It contains various user interface elements such as labels, buttons, and text fields for user interaction.
    Users can enter text, select an encryption/decryption method, and view the encrypted/decrypted text.

    **Methods:**

    * `__init__`: Initializes the application window and sets up the user interface elements.
    * `clear_text_fields`: Clears the input and output text fields.
    * `encrypt_decrypt`: Encrypts or decrypts the entered text depending on the selected method.
    * `prev_action`: Returns the previous action (encryption or decryption).
    * `next_action`: Applies the next action (encryption or decryption).

## Functions:

### Caesar Cipher

* `encode_cesar(msg, sdv)`

    Implements the Caesar cipher algorithm for text encryption.
    - `msg`: The original text message to be encrypted.
    - `sdv`: The shift value for encryption.

* `decode_cesar(line, shif)`

    Implements the Caesar cipher algorithm for text decryption.
    - `line`: The encrypted message to be decrypted.
    - `shif`: The shift value for decryption.

### Vigenère Cipher

* `visiner_encrypt(line, key)`

    Implements the Vigenère cipher algorithm for text encryption.
    - `line`: The original text message to be encrypted.
    - `key`: The keyword for encryption.

* `visiner_decrypt(line, key)`

    Implements the Vigenère cipher algorithm for text decryption.
    - `line`: The encrypted message to be decrypted.
    - `key`: The keyword for decryption.

### Polybius Square

* `encode_poliby(msg, key)`

    Implements the Polybius square cipher algorithm for text encryption.
    - `msg`: The original text message to be encrypted.
    - `key`: The keyword for encryption.

* `decode_polibiya(line2, key)`

    Implements the Polybius square cipher algorithm for text decryption.
    - `line2`: The encrypted message to be decrypted.
    - `key`: The keyword for decryption.

### Anikin Cipher

* `encode_anikin(line, shift)`

    Implements the Anikin cipher algorithm for text encryption.
    - `line`: The original text message to be encrypted.
    - `shift`: The shift value for encryption.

* `decode_anikin(line, shift)`

    Implements the Anikin cipher algorithm for text decryption.
    - `line`: The encrypted message to be decrypted.
    - `shift`: The shift value for decryption.

### Vasilyev Cipher

* `encrypt_vasilyev(text, key)`

    Implements the Vasilyev cipher algorithm for text encryption.
    - `text`: The original text message to be encrypted.
    - `key`: The key for encryption.

* `decrypt_vasilyev(encrypted_text, key)`

    Implements the Vasilyev cipher algorithm for text decryption.
    - `encrypted_text`: The encrypted message to be decrypted.
    - `key`: The key for decryption.

### Levinskiy (Vlad) Cipher

* `encode_vlad(s1, key)`

    Implements the Levinskiy cipher algorithm for text encryption.
    - `s1`: The original text message to be encrypted.
    - `key`: The key for encryption.

* `decode_vlad(s1, key)`

    Implements the Levinskiy cipher algorithm for text decryption.
    - `s1`: The encrypted message to be decrypted.
    - `key`: The key for decryption.

## Additional Methods (in Dialog class)

* `prev_action(self)`

    This function is called when the "Previous Action" button is pressed.
    It retrieves the last action from the list of previous actions and restores the application state by setting the selected encryption method, entered text, and key based on the retrieved data.
    Then the function calls `encrypt_decrypt()` to re-encrypt or re-decrypt the text with the restored parameters.

* `alphabet(self)`

    This function creates and returns a dictionary in which each character from the alphabet is assigned a corresponding numeric value.
    This dictionary is used for encoding and decoding messages in the Levinskiy cipher algorithm.

* `clear_text_fields(self)`

    This function is called when the "Delete Text" button is pressed.
    It clears all input and output text fields in the application.

* `encrypt_decrypt(self)`

    This function is called when the "Encrypt" or "Decrypt" buttons are pressed.
    Depending on the selected encryption method and the sender of the event (the "Encrypt" or "Decrypt" button), the function determines which encryption or decryption algorithm to apply.
    After executing the corresponding algorithm, the function updates the text field with the encrypted/decrypted text.

* `__init__(self)`

    This method initializes the main application window and sets up all user interface elements.
    It sets the window title, geometry, style, places all widgets, sets event handlers for buttons, and populates the dropdown list of encryption methods.

## Used Libraries:

* `sys`: Provides access to some variables used or maintained by the Python interpreter, as well as functions that interact with the interpreter.
* `PyQt6`: Used to create the graphical user interface. In this code, it is used to create GUI elements such as buttons, labels, and text fields.
* `random`: Used to generate random numbers, specifically in the Anikin cipher algorithm for encryption.
