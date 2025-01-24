# Password Strength Evaluator

A simple Python script to evaluate the strength of a password based on length, character variety, and common patterns.

## Features

- Evaluates password length and provides feedback.
- Checks for uppercase and lowercase letter combinations.
- Ensures the inclusion of digits and special characters.
- Detects common weak patterns like "123", "password", and "qwerty".
- Provides an overall strength rating.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mad1fyJourn3y/password_checker.git
   cd password_checker
   ```
2. Run the script:
 ```bash
   python3 password_checker.py -i 
```
## Usage
Run the script in a terminal.
Enter a password when prompted.
Get feedback and suggestions to improve password strength.
## Example
 ```example 
$ python3 password_checker.py -i
Enter a password to test its strength: MyP@ssw0rd!
Overall strength: Strong.
$ python3 password_checker.py -i
Enter a password to test its strength: mypassword
Use a mix of uppercase and lowercase letters.
Include at least one number.
Include at least one special character.
Avoid using common patterns or words like 'password' or '123'.
Overall strength: Weak. 
```
## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any inquiries, feel free to reach out:

GitHub: mad1fyJourn3y
Email: ninitekali@gmail.com
