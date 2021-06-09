class AppErrorBaseClass(Exception):
    pass

class ObjectNotFound(AppErrorBaseClass):
    pass

def get(self, anime_id):
    anime = Anime.get_by_id(anime_id)
    if anime is None:
        raise ObjectNotFound('El Anime no existe')
    resp = anime_schema.dump(anime)
    return resp