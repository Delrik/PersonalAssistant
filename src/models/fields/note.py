class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag.lower())

    def is_exist(self, tag):
        return tag.lower() in self.tags

    def __str__(self):
        return f"Note: {self.title}, text: {self.text}, tags: {", ".join(self.tags)}"
