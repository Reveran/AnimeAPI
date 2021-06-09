from app.db import db, BaseModelMixin

class Anime(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    slug = db.Column(db.String)
    id2 = db.Column(db.Integer)
    kind = db.Column(db.String)
    def __init__(self, title, slug, id2, kind):
        self.title = title
        self.slug = slug
        self.id2 = id2
        self.kind = kind
    def __repr__(self):
        return f'Anime({self.title})'
    def __str__(self):
        return f'{self.title}'
