def parse_input(user_input):
    cmd, *args = user_input.split("/")
    cmd = cmd.strip().lower()
    args = [a.lower().strip() for a in args]
    return cmd, *args
