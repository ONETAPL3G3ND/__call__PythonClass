class Comment:
    def __init__(self):
        self.comments = []

    def _AddComment(self, text):
        self.comments.append(text)

    def __call__(self, comment):
        print(f"New comment: {comment}")
        self._AddComment(comment)

    def GetComments(self):
        return self.comments


if __name__ == "__main__":
    comment = Comment()
    comment("Hi")
    comment("Hallo")
    comment("how old are you?")
    print(comment.GetComments())