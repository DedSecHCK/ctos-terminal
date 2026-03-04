#!/usr/bin/env python3
"""
CTOS Terminal - A powerful futuristic multi-purpose terminal
Styled like Kali, Debian, Parrot, and Manjaro terminals.
Portable and multi-purpose.
"""

import sys
import os
import socket
from datetime import datetime
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import FormattedText
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
from rich.spinner import Spinner
from pyfiglet import Figlet
import subprocess
import time
try:
    import git
except ImportError:
    git = None

console = Console()

COLORS = {
    'prompt': 'ansigreen bold',
    'input': 'ansigreen',
    'banner': 'bold green',
    'border': 'green',
    'error': 'red',
    'success': 'green',
}

BUILTIN_COMMANDS = {
    'help': 'Show available commands',
    'clear': 'Clear the screen',
    'exit': 'Exit the terminal',
    'quit': 'Exit the terminal',
    'ctos-info': 'Show CTOS information',
}

def get_hostname():
    return socket.gethostname()

def get_username():
    return os.getenv('USER') or os.getenv('USERNAME') or 'user'

def get_current_dir():
    cwd = os.getcwd()
    home = os.path.expanduser('~')
    if cwd == home:
        return "🏠 home"
    else:
        if cwd.startswith(home):
            cwd = cwd.replace(home, '~', 1)
        return f"📁 {cwd}"

def get_git_info():
    if not git:
        return None
    try:
        repo = git.Repo(search_parent_directories=True)
        branch = repo.active_branch.name
        dirty = '✗' if repo.is_dirty() else '✓'
        return f"git:{branch} {dirty}"
    except:
        return None

def get_time():
    return datetime.now().strftime('%H:%M:%S')

def display_banner():
    with console.status("[bold green]Loading CTOS Terminal...", spinner="dots") as status:
        time.sleep(1)  # Simulate loading
    f = Figlet(font='slant')
    banner = f.renderText('CTOS Terminal')
    console.print(Panel.fit(banner, title=f"[bold red]Welcome to CTOS - {get_username()}@{get_hostname()}[/bold red]", border_style="blue"))

def execute_builtin(command):
    if command == 'help':
        console.print("[bold cyan]Available commands:[/bold cyan]")
        for cmd, desc in BUILTIN_COMMANDS.items():
            console.print(f"  {cmd}: {desc}")
        return True
    elif command == 'clear':
        console.clear()
        display_banner()
        return True
    elif command == 'ctos-info':
        console.print(Panel.fit("CTOS Terminal v1.0\nA futuristic multi-purpose terminal\nStyled like Kali, Debian, Parrot, Manjaro", title="[bold blue]Info[/bold blue]"))
        return True
    return False

def execute_command(command):
    if execute_builtin(command):
        return
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            console.print(result.stdout.rstrip())
        if result.stderr:
            console.print(f"[{COLORS['error']}]{result.stderr.rstrip()}[/{COLORS['error']}]")
    except Exception as e:
        console.print(f"[{COLORS['error']}]Error: {e}[/{COLORS['error']}]")

def get_bottom_toolbar():
    git_info = get_git_info()
    toolbar = f"Dir: {get_current_dir()} | Time: {get_time()}"
    if git_info:
        toolbar += f" | {git_info}"
    return toolbar

def main():
    display_banner()
    
    
    style = Style.from_dict(COLORS)
    
    
    completer = WordCompleter(list(BUILTIN_COMMANDS.keys()) + ['ls', 'pwd', 'cd', 'echo', 'cat', 'grep'])
    
    session = PromptSession(
        style=style, 
        completer=completer,
        bottom_toolbar=get_bottom_toolbar,
        refresh_interval=1  
    )
    
    while True:
        try:
            
            prompt_parts = [
                ('class:prompt', f'[{get_current_dir()}] > ')
            ]
            user_input = session.prompt(FormattedText(prompt_parts))
            if user_input.lower() in ['exit', 'quit']:
                break
            elif user_input.strip() == '':
                continue
            else:
                execute_command(user_input)
        except KeyboardInterrupt:
            console.print("\n[bold yellow]Interrupted. Type 'exit' to quit.[/bold yellow]")
            continue
        except EOFError:
            break
    
    console.print(f"[{COLORS['success']}]Goodbye from CTOS![/{COLORS['success']}]")

if __name__ == "__main__":
    main()
