def linear_search_profiles(profiles, query):
    results = []

    query = query.strip().lower()

    for profile in profiles:

        full_name = profile.fullName.lower()
        username = profile.username.lower()
        college = profile.college.lower()
        department = profile.department.lower()

        if (
            query in full_name
            or query in username
            or query in college
            or query in department
        ):
            results.append(profile)

    return results