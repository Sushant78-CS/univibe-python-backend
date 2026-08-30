from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    profileId: int | None = None
    interests: list[str] = Field(default_factory=list)
    department: str | None = None
    year: str | None = None


class RecommendationRequest(BaseModel):
    user: UserProfile
    candidates: list[UserProfile]


class RecommendationResult(BaseModel):
    profileId: int
    score: float


class RecommendationResponse(BaseModel):
    recommendations: list[RecommendationResult]