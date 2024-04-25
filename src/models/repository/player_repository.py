from src.models.entities.players import Player


def generate_player():
    create_name = 'Arthur Silva'
    create_age = 22
    create_email = 'arthursilva70@outlook.com'
    create_password = '85690368P.v'

    return {
        'full_name': create_name,
        'age': create_age,
        'email': create_email,
        'password': create_password
    }


def get_player_by_id():
    ...


gen = generate_player()
p1 = Player(**gen)
print(p1)
