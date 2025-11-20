# Mnemonic — NATO Phonetic Password Mnemonic Converter

Convert any password or phrase into an easy-to-read NATO phonetic mnemonic. Each character is printed as a single mnemonic word (e.g., `A` → `Capital Alpha`, `a` → `Alpha`, `!` → `Exclamation Mark`).

This tool can also fetch a strong password from Dinopass and convert it on the fly.


## Features
- Convert any input (letters, digits, punctuation, spaces) into mnemonic words
- Treat multiple CLI tokens as one password or split them into separate ones
- Optionally fetch a strong password from Dinopass (`-p/--password`)
- Simple CLI interface with clear exit statuses


## Requirements
- Python 3.8+ (tested with modern Python 3 versions)
- Internet access only if you use the `-p/--password` flag (to reach Dinopass)


## Getting Started
You can run the tool directly with Python (no install required), or build a standalone executable using the provided PyInstaller spec.

### Run with Python
```bash
# From the project root
python mnemonic.py --help

# Convert a phrase (tokens are joined with a single space by default)
python mnemonic.py My super secret

# Treat each token as a separate password (-s/--split)
python mnemonic.py --split alpha beta

# Fetch a strong password from Dinopass and convert it (-p/--password)
python mnemonic.py --password

# Print version
python mnemonic.py --version
```

### Build a standalone binary (optional)
A PyInstaller spec is included: `mnemonic.spec`.

```bash
# Requires: pip install pyinstaller
pyinstaller mnemonic.spec

# The binary will be in ./dist/mnemonic
./dist/mnemonic --help
```


## Command-line Reference
```text
usage: mnemonic.py [-h] [-v] [-s] [-p] [phrase ...]

Convert a password into a mnemonic phrase.

positional arguments:
  phrase                Password to convert. If multiple tokens are provided, they are joined with a single space unless --split is used.

options:
  -h, --help            Show this help message and exit
  -v, --version         Show program version and exit
  -s, --split           Do not combine multiple space-split words into one password; treat each token as a separate password
  -p, --password        Fetch a strong password from Dinopass and convert it
```


## Exit Status
- `0` — Success
- `1` — Dinopass could not be reached or returned an invalid password length (when using `-p/--password`)


## Notes on Mnemonics
- Uppercase letters map to the word "Capital" + NATO (e.g., `A` → `Capital Alpha`).
- Lowercase letters map to standard NATO (e.g., `a` → `Alpha`).
- Digits and common punctuation are supported (e.g., `!` → `Exclamation Mark`, space → `Space`).


## Examples
```bash
# Version
python mnemonic.py -v

# Basic phrase (joined):
python mnemonic.py My super secret

# Split tokens (printed as separate blocks):
python mnemonic.py -s alpha beta

# Generate a strong password from Dinopass and convert it:
python mnemonic.py -p
```

Example output snippet:
```text
My super secret

Capital Mike
yankee
Space
sierra
uniform
papa
echo
romeo
Space
sierra
echo
charlie
romeo
echo
tango
```


## Development
- Entry point: `mnemonic.py`
- Version: `2.0.0`
- Packaging: `mnemonic.spec` (PyInstaller)

Suggested setup:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install pyinstaller
```

Run locally:
```bash
python mnemonic.py "Your P@ssw0rd!"
```


## Security Considerations
- Be mindful when displaying or recording passwords (mnemonics reveal character classes and lengths).
- When using `-p/--password`, your system will make an HTTP request to `https://dinopass.com/password/strong`. Ensure you are comfortable with this in your environment.


## Acknowledgments
This project uses the excellent API provided by Dinopass (https://dinopass.com/) and Codemoji Inc. (https://www.codemoji.com/) for generating new passwords. Please visit their websites and show your support.

## License
This repository did not include a license file at the time this README was generated. If a license is later added, that file governs usage.
