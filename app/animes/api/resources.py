from flask import Blueprint
from flask_restful import Api, Resource
from .schemas import AnimeSchema
from ..models import Anime
from random import randint

animes_bp = Blueprint('anime_bp', __name__)
anime_schema = AnimeSchema()
api = Api(animes_bp)

class AnimeListResource(Resource):
    def get(self):
        animes = Anime.get_all()
        result = anime_schema.dump(animes, many=True)
        return result

class AnimeResource(Resource):
    def get(self, anime_id):
        anime = Anime.get_by_id(anime_id)
        resp = anime_schema.dump(anime)
        return resp

class AnimeRandomResource(Resource):
    def get(self):
        anime = Anime.get_by_id(randint(0,3473))
        resp = anime_schema.dump(anime)
        return resp

api.add_resource(AnimeListResource, '/api/anime/all/', endpoint='anime_list_resource')
api.add_resource(AnimeResource, '/api/anime/<int:anime_id>', endpoint='anime_resource')
api.add_resource(AnimeRandomResource, '/api/anime/', endpoint='anime_Random_resource')

