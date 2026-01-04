from pydantic import BaseModel


# this is the model for the Person entity
# it is used to validate the request body for the POST /api/people endpoint
class Person(BaseModel):
  id: str # the id of the person
  name: str # the name of the person
  title: str # the title of the person
