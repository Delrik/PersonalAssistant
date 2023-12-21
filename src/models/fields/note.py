class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tags = []

    def add_tag(self, tag):
        if tag in self.tags:
            raise KeyError(f"This tag '{tag}' already exists.")
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags = list(filter(lambda x: x != tag, self.tags))

    def __str__(self):
        return f"Note: {self.title}, text: {self.text}, tags: {", ".join(self.tags)}"
