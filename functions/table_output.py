from colorama import Back, Fore


def table_output(lines, type):
    heading_types = {
        "commands": ["input", "description"],
        "employee_info": ["name", "position", "birthday date", "age"],
        "employee_birthday": ["name", "birthday date"],
    }

    color = {
        "fore": {
            "commands": Fore.MAGENTA,
            "employee_info": Fore.LIGHTCYAN_EX,
            "employee_birthday": Fore.LIGHTYELLOW_EX,
        },
        "back": {
            "commands": Back.MAGENTA,
            "employee_info": Back.LIGHTCYAN_EX,
            "employee_birthday": Back.LIGHTYELLOW_EX,
        },
    }

    headings = heading_types.get(type, [])

    if not headings:
        return "invalid type"

    lines = [line.split(" - ") for line in lines]

    max_lengths = [
        max(
            len(headings[i]),
            max(len(line[i]) if len(line) > i else 0 for line in lines),
        )
        for i in range(len(headings))
    ]

    formatted_headings = " | ".join(
        f"{color['back'][type]}{Fore.BLACK}{headings[i]:<{max_lengths[i]}}{color['fore'][type]}{Back.RESET}"
        for i in range(len(headings))
    )

    hyphen_line = " | ".join(f"{color['fore'][type]}-" * max_lengths[i] for i in range(len(headings)))

    formatted_lines = [
        " | ".join(
            f"{line[i]:<{max_lengths[i]}}" if len(line) > i else line[i]
            for i in range(len(headings))
        )
        for line in lines
    ]

    formatted_with_lines = [
        f"{color['fore'][type]}{formatted_lines[i]}\n{hyphen_line}{Fore.RESET}"
        for i in range(len(formatted_lines))
    ]

    return "\n".join(
        [hyphen_line, formatted_headings, hyphen_line] + formatted_with_lines
    )
