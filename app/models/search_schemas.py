from pydantic import BaseModel


class SearchProfile(BaseModel):
    profileId: int
    fullName: str
    username: str
    college: str
    department: str


class SearchRequest(BaseModel):
    query: str
    profiles: list[SearchProfile]


class SearchResponse(BaseModel):
    results: list[SearchProfile]
    algorithm: str
    timeComplexity: str