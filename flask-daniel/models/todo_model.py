class Todo:
    def __init__(self, id, title, status):
        self.id = id
        self.title = title
        self.status = status

    def to_dict(self):
        return {"id":self.id, "title": self.title, "status": self.status}
