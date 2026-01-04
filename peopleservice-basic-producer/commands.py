from pydantic import BaseModel

# this is request body for the POST /api/people endpoint

class CreatePeopleCommand(BaseModel):
  count: int

