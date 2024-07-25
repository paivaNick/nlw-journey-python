
class TripConfirmer:
    def __init__(self, trips_repository):
        self.__trips_repository = trips_repository

    def confirm(self,trip_id):
        try:
            self.__trips_repository.update_trip_status(trip_id)
            return {
                    "body": {
                            'error': None
                        }, 
                    "status_code": 204}
        except Exception as exception:
                return {
                        "body": {
                            "error": {"bad request": str(exception)}
                        },
                        "status_code": 400
                        }
