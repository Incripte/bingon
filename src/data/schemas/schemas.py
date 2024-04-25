def individual_serial(player) -> dict:
    return {
        "id": str(player["_id"]),
        "full_name": str(player["full_name"]),
        "age": int(player["age"]),
        "email": str(player["email"]),
        "password": str(player["password"])
    }


def list_serial(players) -> list:
    return [individual_serial(player) for player in players]
