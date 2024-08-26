import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from courses.models import Course
from reviews.models import Review

def get_course_recommendations(user_id):
    reviews = Review.objects.all().values('course', 'rating')
    reviews_df = pd.DataFrame(reviews)
    courses = Course.objects.all().values('id', 'title', 'description')
    courses_df = pd.DataFrame(courses)

    ratings_matrix = reviews_df.pivot_table(index='course', columns='rating', values='rating')
    ratings_matrix = ratings_matrix.fillna(0)

    similarity_matrix = cosine_similarity(ratings_matrix.T)
    similarity_df = pd.DataFrame(similarity_matrix, index=ratings_matrix.columns, columns=ratings_matrix.columns)

    user_ratings = reviews_df[reviews_df['student'] == user_id]
    user_rated_courses = user_ratings['course'].tolist()

    recommendations = {}
    for course_id in user_rated_courses:
        similar_courses = similarity_df[course_id].sort_values(ascending=False)
        for similar_course, similarity_score in similar_courses.items():
            if similar_course not in user_rated_courses:
                if similar_course not in recommendations:
                    recommendations[similar_course] = similarity_score
                else:
                    recommendations[similar_course] += similarity_score

    recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    recommended_course_ids = [rec[0] for rec in recommendations]
    recommended_courses = Course.objects.filter(id__in=recommended_course_ids)

    return recommended_courses
