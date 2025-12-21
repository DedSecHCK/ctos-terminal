# CTOS Terminal

A powerful, futuristic multi-purpose terminal inspired by Kali Linux, Debian, Parrot OS, and Manjaro.

## Features

- Interactive shell with command execution
- Futuristic UI with rich text, colors, and animations
- Customizable prompt styled like Manjaro
- Built-in commands (help, clear, ctos-info)
- Autocomplete for common commands
- Portable across platforms

## Installation

### Windows
1. Install Python 3.8+
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

### Debian/Ubuntu/Linux
1. Update system: `sudo apt update`
2. Install Python and pip: `sudo apt install python3 python3-pip`
3. Install dependencies: `pip3 install -r requirements.txt`
4. Make executable: `chmod +x main.py`
5. Run: `./main.py` or `python3 main.py`

For portability, you can copy the script and requirements.txt to any Linux system with Python installed.

## Usage

Run the terminal and enter commands at the prompt.

Built-in commands:
- `help`: Show available commands
- `clear`: Clear the screen
- `ctos-info`: Show CTOS information
- `exit` or `quit`: Exit the terminal

## Customization

Modify `main.py` to change colors, add more built-in commands, or customize the prompt.