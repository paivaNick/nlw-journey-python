import uuid
class LinkCreator:
    def __init__(self,link_repository):
        self.__link_repository = link_repository

    def create(self, body, trip_id):
        try:
            link_id = str(uuid.uuid4())
            links_infos = {
                    "link": body["url"],
                    "title": body["title"],
                    "id": link_id,
                    "trip_id": trip_id
                    }
            self.__link_repository.register_link(links_infos)
         
            return {
                    "body": {"linkId": link_id},
                    'status_code': 201
                    }
        except Exception as exception:
                return {
                        "body": {
                            "error": {"bad request": str(exception)}
                        },
                        "status_code": 400
                        }

