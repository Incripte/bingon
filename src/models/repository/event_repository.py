# from src.models.entities.event import Event


def generate_event():
    event_name = 'Evento Teste'
    start_event = '25/05/2024 20:00:00'
    max_attendees = 100
    cartels_sold = 172

    return {
        'id': 12,
        'event_name': event_name,
        'start_event': start_event,
        'max_attendees': max_attendees,
        'cartels_sold': cartels_sold
    }


def get_event_by_id(event_id):
    try:
        ...

    except Exception as exception:
        exception = 'Deu merda no barraco'
        return exception


get_event_by_id(12)
