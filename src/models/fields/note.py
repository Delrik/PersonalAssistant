from rich.text import Text


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag.lower())

    def is_exist(self, tag):
        return tag.lower() in self.tags

    def __rich__(self):
        formattedn_notes = Text()
        formattedn_notes.append("Title: ", style="white")
        formattedn_notes.append(f"{self.title}\n", style="blue")
        formattedn_notes.append("Text: ", style="white")
        formattedn_notes.append(f"{self.text}\n", style="blue")

        if self.tags:
            formattedn_notes.append("Tags: ", style="white")
            formattedn_notes.append(f"{', '.join(self.tags)}\n", style="green")

        return formattedn_notes
