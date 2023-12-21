class Note:
    def __init__(self, title, note):
        self.title = title
        self.note = note
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags = list(filter(lambda x: x != tag, self.tags))

    def __str__(self):
        return f"Note: {self.title}, note: {self.note}, tags: {", ".join(self.tags)}"
