def calculate_similarity(
    user_interests: list[str],
    candidate_interests: list[str],
    user_department: str | None,
    candidate_department: str | None,
    user_year: str | None,
    candidate_year: str | None,
):
    user_set = {
        interest.strip().lower()
        for interest in user_interests
    }

    candidate_set = {
        interest.strip().lower()
        for interest in candidate_interests
    }

    # Interest similarity
    if user_set or candidate_set:
        union = user_set | candidate_set

        if union:
            interest_score = (
                len(user_set & candidate_set) /
                len(union)
            )
        else:
            interest_score = 0
    else:
        interest_score = 0

    # Department similarity
    department_score = 0

    if (
        user_department
        and candidate_department
        and user_department.lower()
        == candidate_department.lower()
    ):
        department_score = 1

    # Year similarity
    year_score = 0

    if (
        user_year
        and candidate_year
        and user_year.lower()
        == candidate_year.lower()
    ):
        year_score = 1

    # Final weighted score
    final_score = (
        interest_score * 0.70
        + department_score * 0.20
        + year_score * 0.10
    )

    return round(final_score, 3)