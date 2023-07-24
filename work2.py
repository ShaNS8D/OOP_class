class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def scoring_method(self, lecturer, course, grades):    
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
            and course in self.courses_in_progress:
            if course in lecturer.dict_grades_lecturer:
                lecturer.dict_grades_lecturer[course] += [grades]
            else:
                lecturer.dict_grades_lecturer[course] = [grades]
        else:
            print('Ошибка')

        
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.dict_grades_lecturer = {}


class Lecturer (Mentor):
    pass


class Reviewer (Mentor):
            
    def add_grades_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and\
            course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 