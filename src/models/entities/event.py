from pydantic import BaseModel


class Event(BaseModel):
    event_name: str
    start_event: str
    max_attendees: int
    cartels_sold: int

    def __repr__(self):
        return f'Cartela ref. event [{self.event_name}], '\
            f'Start [{self.start_event}], '\
            f'Max attendees: [{self.max_attendees}], '\
            f'Cartels Sold: [{self.cartels_sold}]'
