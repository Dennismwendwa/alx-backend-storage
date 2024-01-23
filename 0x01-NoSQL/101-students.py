#!/usr/bin/env python3
"""This script sort all students by average score"""


def top_students(mongo_collection):
    """Finding the everage of each students score"""
    students_with_avg = mongo_collection.aggregate(
        [
            {
                "$project": {
                    "_id": 1,
                    "name": 1,
                    "averageScore": {
                        "$avg": {
                            "$avg": "$topics.score",
                        },
                    },
                    "topics": 1,
                },
            },
            {
                "$sort": {"averageScore": -1},
            },
        ]
    )
    return students_with_avg
