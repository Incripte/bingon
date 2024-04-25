from pydantic import BaseModel


class Player(BaseModel):
    full_name: str
    age: int
    email: str
    password: str

    def __repr__(self):
        return f'Full name [{self.full_name}], Age [{self.age}]'
