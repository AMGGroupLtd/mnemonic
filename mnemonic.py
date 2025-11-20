import argparse
import sys
import urllib.request

"""Mnemonic converter for passwords.

This module converts a password (or a generated one) into a mnemonic using
NATO phonetic words, printing one mnemonic word per character. It can accept
one or more tokens as a positional phrase, optionally splitting them into
separate passwords to process. It can also fetch a strong password from
Dinopass when requested.

Features
- Positional `phrase` accepts zero or more tokens. By default, multiple tokens
  are joined with a single space and treated as one password.
- `-s` / `--split` treats each provided token as a separate password and
  prints a blank line between each output block.
- `-p` / `--password` fetches a strong password from
  https://dinopass.com/password/strong and converts it.
- `-v` / `--version` shows the program version and exits.

Examples
  $ python mnemonic.py -v
  $ python mnemonic.py My super secret
  $ python mnemonic.py -s alpha beta
  $ python mnemonic.py -p

Exit status
- 0 on success
- 1 if Dinopass cannot be reached or returns an invalid password length

Note: Using `-p/--password` requires internet access to reach Dinopass.
"""


__author__ = "Matt Lowe <marl.scot.1@googlemail.com"
__version__ = "2.1.0"

nato = {
    " ": "Space",
    "!": "Exclamation Mark",
    '"': "Quotation Mark",
    "#": "Hash",
    "$": "Dollar Sign",
    "%": "Percent",
    "&": "Ampersand",
    "'": "Apostrophe",
    "(": "Left Parenthesis",
    ")": "Right Parenthesis",
    "*": "Asterisk",
    "+": "Plus",
    ",": "Comma",
    "-": "Hyphen",
    ".": "Period",
    "/": "Slash",

    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",

    ":": "Colon",
    ";": "Semicolon",
    "<": "Less Than",
    "=": "Equals",
    ">": "Greater Than",
    "?": "Question Mark",
    "@": "At Sign",

    # NATO A–Z
    "A": "Capital Alpha",
    "B": "Capital Bravo",
    "C": "Capital Charlie",
    "D": "Capital Delta",
    "E": "Capital Echo",
    "F": "Capital Foxtrot",
    "G": "Capital Golf",
    "H": "Capital Hotel",
    "I": "Capital India",
    "J": "Capital Juliett",
    "K": "Capital Kilo",
    "L": "Capital Lima",
    "M": "Capital Mike",
    "N": "Capital November",
    "O": "Capital Oscar",
    "P": "Capital Papa",
    "Q": "Capital Quebec",
    "R": "Capital Romeo",
    "S": "Capital Sierra",
    "T": "Capital Tango",
    "U": "Capital Uniform",
    "V": "Capital Victor",
    "W": "Capital Whiskey",
    "X": "Capital X-ray",
    "Y": "Capital Yankee",
    "Z": "Capital Zulu",

    "[": "Left Bracket",
    "\\": "Backslash",
    "]": "Right Bracket",
    "^": "Caret",
    "_": "Underscore",
    "`": "Backtick",

    # lowercase letters → same NATO
    "a": "Alpha",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whiskey",
    "x": "X-ray",
    "y": "Yankee",
    "z": "Zulu",

    "{": "Left Brace",
    "|": "Vertical Bar",
    "}": "Right Brace",
    "~": "Tilde",
}

def main():
    parser = argparse.ArgumentParser(description="Convert a password into a mnemonic phrase.")
    parser.add_argument("phrase", nargs="*", help="Password to convert.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("-s", "--split", action="store_true", help="Do not combine multiple space split words into one mnemonic word.")
    parser.add_argument("-p", "--password", action="store_true", help="Generate a password and convert it.")

    args = parser.parse_args()

    input_strings = []

    if args.password:
        print("Generating password...")
        f = urllib.request.urlopen('https://dinopass.com/password/strong')
        if f.getcode() != 200:
            print(f"Unable to generate password from Dinopass. Error code : {f.getcode()}")
            sys.exit(1)
        print("Password generated.")
        phrase = f.readline().decode('utf-8').strip()
        if len(phrase) < 10 or len(phrase) > 64:
            print("Dinopass returned an invalid password length. Please try again, and if you still get this error, check the server.")
            sys.exit(1)
        input_strings = [phrase]
    else:
        if not args.phrase:
            parser.error("the following arguments are required: phrase (or use -p/--password to generate one)")
        if args.split:
            input_strings = args.phrase
        else:
            input_strings = [" ".join(args.phrase)]

    for idx, password in enumerate(input_strings):
        if idx != 0:
            print("\n")
        mnemonic = ([nato[char] for char in password])
        print(f"{password}\n")
        print("\n".join(mnemonic))

if __name__ == "__main__":
    main()