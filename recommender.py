def score_college(college, user):
    score = 0

    if user["specialization"].lower() in college.specialization.lower():
        score += 40

    score += (100 - college.ranking)

    if user["budget"] == "Low" and college.tuition < 100000:
        score += 20
    elif user["budget"] == "Medium" and college.tuition < 1000000:
        score += 10

    if user.get("filters", {}).get("scholarship") and college.scholarship:
        score += 10

    return score
