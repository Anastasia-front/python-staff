from colorama import Back, Fore


def table_output(lines, type):
    heading_types = {
        "commands": ["input", "description"],
        "employee_info": ["name", "position", "birthday date", "age"],
        "employee_birthday": ["name", "birthday date"],
    }

    headings = heading_types.get(type, [])

    if not headings:
        return "invalid type"

    lines = [line.split(" - ") for line in lines]

    max_lengths = [
        max(len(line[i]) if len(line) > i else 0 for line in lines)
        for i in range(len(headings))
    ]

    formatted_headings = " | ".join(
        f"{Back.MAGENTA}{Fore.BLACK}{headings[i]:<{max_lengths[i]}}{Fore.RESET}{Back.RESET}"
        for i in range(len(headings))
    )

    hyphen_line = " | ".join("-" * max_lengths[i] for i in range(len(headings)))

    formatted_lines = [
        " | ".join(
            f"{line[i]:<{max_lengths[i]}}" if len(line) > i else line[i]
            for i in range(len(headings))
        )
        for line in lines
    ]

    formatted_with_lines = [
        f"{Fore.MAGENTA}{formatted_lines[i]}\n{hyphen_line}{Fore.RESET}"
        for i in range(len(formatted_lines))
    ]

    return "\n".join(
        [hyphen_line, formatted_headings, hyphen_line] + formatted_with_lines
    )
