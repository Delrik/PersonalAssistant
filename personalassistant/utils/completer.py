from prompt_toolkit.completion import Completer, Completion


class CommandCompleter(Completer):
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lstrip()

        if " " in text_before_cursor:
            return

        current_word = document.get_word_before_cursor(WORD=True)

        commands = [
            "add-address",
            "add-birthday",
            "add-email",
            "add-note",
            "add-phone",
            "add-tag",
            "add",
            "all",
            "birthdays",
            "change-address",
            "change-birthday",
            "change-email",
            "change-note-title",
            "change-note",
            "change-phone",
            "change",
            "close",
            "find",
            "exit",
            "find-note",
            "find-tag",
            "hello",
            "help",
            "phone",
            "remove",
            "remove-address",
            "remove-birthday",
            "remove-email",
            "remove-note",
            "remove-phone",
        ]

        for command in commands:
            if command.startswith(current_word.lower()):
                yield Completion(command, start_position=-len(current_word))
