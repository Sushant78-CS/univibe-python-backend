from fastapi import FastAPI

from app.models.schemas import RecommendationResponse, RecommendationRequest, RecommendationResult
from app.algorithms.recommendation import calculate_similarity
from app.models.search_schemas import SearchRequest, SearchResponse
from app.algorithms.linear_search import linear_search_profiles
from app.algorithms.merge_sort import merge_sort

app = FastAPI(
    title="UniVibe API",
    description="Backend API for UniVibe campus community",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Welcome to the UniVibe API",
        "status": "running"
    }


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post(
    "/recommend",
    response_model=RecommendationResponse
)
def recommend(request: RecommendationRequest):

    results = []

    for candidate in request.candidates:

        if candidate.profileId is None:
            continue

        score = calculate_similarity(
            request.user.interests,
            candidate.interests,
            request.user.department,
            candidate.department,
            request.user.year,
            candidate.year,
        )

        results.append(
            RecommendationResult(
                profileId=candidate.profileId,
                score=score,
            )
        )

    # Highest compatibility first
    results = merge_sort(results)

    return RecommendationResponse(
        recommendations=results
    )

@app.post(
    "/search",
    response_model=SearchResponse
)
def search_profiles(request: SearchRequest):

    results = linear_search_profiles(
        request.profiles,
        request.query
    )

    return SearchResponse(
        results=results,
        algorithm="Linear Search",
        timeComplexity="O(n)"
    )