from typing import Dict

class TripFinder: 
    def __init__(self, trip_repository):
        self.__trip_repository = trip_repository

    def find_trip_details(self,trip_id) -> Dict:
        try:       
            trip = self.__trip_repository.find_trip_by_id(trip_id)
            if not trip:
                raise Exception("no trip found")

            return {
                    "body": {
                        'trip': {
                            'id': trip[0],
                            'destination': trip[1],
                            'starts_at': trip[2],
                            'ends_at': trip[3],
                            'status': trip[6]
                            }
                        },
                    'status_code': 200
                    }
        except Exception as exception:
            return {
                    "body": {
                        'error': "bad request",
                        "message": str(exception)
                        },
                    'status_code': 400
                    }
