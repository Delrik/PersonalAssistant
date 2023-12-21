from prompt_toolkit.completion import WordCompleter


# TODO add all possible commands
def get_command_completer():
    command_completer = WordCompleter(
        ["close", "exit", "hello", "add", "change", "phone", "all"], ignore_case=True
    )
    return command_completer
