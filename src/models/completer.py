from prompt_toolkit.completion import Completer, Completion


class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lstrip()

        if " " in text_before_cursor:
            return

        current_word = document.get_word_before_cursor(WORD=True)

        commands = [
            "close",
            "exit",
            "hello",
            "add",
            "change",
            "phone",
            "all",
        ]  # TODO add all commands

        for command in commands:
            if command.startswith(current_word.lower()):
                yield Completion(command, start_position=-len(current_word))
