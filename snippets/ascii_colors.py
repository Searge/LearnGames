# -*- coding: utf-8 -*-
# https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
from typing import Dict

ENDCOLOR: str = '\033[0m'
DEFAULT: str = '\033[99m'
BRIGHT_COLORS: Dict[str, str] = {
    'Black': '\033[90m',
    'Red': '\033[91m',
    'Green': '\033[92m',
    'Yellow': '\033[93m',
    'Blue': '\033[94m',
    'Magenta': '\033[95m',
    'Cyan': '\033[96m',
    'White': '\033[97m'
}


def ascii_colors(colors: Dict[str, str]) -> None:
    for color, code in colors.items():
        # adding ten for background color
        bg = f'{code[:2]}{int(code[-3:-1]) + 10}{code[-1]}'
        print(f'{bg}{color} {ENDCOLOR} — {code}{color}{ENDCOLOR}')


if __name__ == "__main__":
    ascii_colors(BRIGHT_COLORS)
