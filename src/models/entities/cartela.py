from pydantic import BaseModel


class Cartela(BaseModel):
    id: str
    event_name: str
    amount: float
    numbers: dict

    def __repr__(self):
        return f'Cartela ref. event [{self.event_name}], '\
            f'Value [{self.amount}]'
