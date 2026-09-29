from typing import List
from college import Student, Course
import utils

def calculate_gpa(student: Student, courses: List[Course]) -> float:
    '''
    i first examine every course and check
    whether the given student has a grade in that course 
    for this courses i cconvert the letter grade to points using Course.convert_grade_to_points
    then multiply by the course's credit hours and add it to the numerator 
    i also sumthe hours of the courses attended by the student for the denominator 
    if a student has no valid course grades the GPA is defined as 0.0.
    '''
    weighted_points: float = 0.0
    total_hours: int = 0

    for course in courses:
        grade = course.grades.get(student.id)
        if grade is not None:
            points = Course.convert_grade_to_points(grade)
            weighted_points += course.hours * points
            total_hours += course.hours

    if total_hours == 0:
        return 0.0

    return weighted_points / total_hours