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
1. Clone or download the repository: `git clone https://github.com/DedSecHCK/ctos-terminal.git`
2. Make install script executable: `chmod +x install.sh`
3. Run the install script: `sudo ./install.sh`
   Or manually:
   - `sudo apt update`
   - `sudo apt install python3 python3-pip`
   - `pip3 install -r requirements.txt`
   - `chmod +x main.py`
4. Run: `./main.py` or `python3 main.py`

**For daily use**: The install script copies CTOS to `/usr/local/bin/ctos`, so you can run `ctos` from anywhere.

**Uninstall**: `sudo rm /usr/local/bin/ctos && rm -rf ~/ctos-terminal && pip3 uninstall -r requirements.txt` (optional, removes dependencies).

**Note**: If you get "command not found" for `./install.sh`, ensure it's executable with `chmod +x install.sh`. If cloned from Git, run `git config core.autocrlf false` to fix line endings on Windows clones.

For portability, you can copy the script and requirements.txt to any Linux system with Python installed.

## GitHub

The project is hosted on GitHub. To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "Description"`
4. Push to branch: `git push origin feature-name`
5. Create a Pull Request

## Usage

Run the terminal and enter commands at the prompt.

Built-in commands:
- `help`: Show available commands
- `clear`: Clear the screen
- `ctos-info`: Show CTOS information
- `exit` or `quit`: Exit the terminal

## Customization

Modify `main.py` to change colors, add more built-in commands, or customize the prompt.