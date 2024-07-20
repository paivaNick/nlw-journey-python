from typing import Dict, List, Tuple
from sqlite3 import Connection


class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def register_email(self, email_infos: Dict) -> None:
        cursor = self.__conn.cursor()

        cursor.execute(
            """
                INSERT INTO emails_to_invite
                    (id, trip_id,email)
                VALUES
                    (?,?,?)

            """, (
                email_infos["id"],
                email_infos["trip_id"],
                email_infos["email"]
            )
        )
        self.__conn.commit()
    
    def find_email_from_trip(self, trip_id: str):
        cursor = self.__conn.cursor()
        cursor.execute(
                """
                    SELECT * FROM trips WHERE id = ?

                """, (trip_id,)
                )
        email = cursor.fetchall()
        return email


