class Mentor:

    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.dict_grades_lecturer = {}
        self.average_grade = 0


class Student:

    def __init__(self,name,surname,gender,):
        self.name=name
        self.surname = surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_dict_student = {}
        self.average_grade = 0

    def average_grade_student(self):
        grade_list=[]
        for val in self.grades_dict_student.values():
            grade_list.extend(val)
        sum_=sum(grade_list)
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    def scoring_method(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
            and course in self.courses_in_progress:
            if course in lecturer.dict_grades_lecturer:
                lecturer.dict_grades_lecturer[course] += [grades]
            else:
                lecturer.dict_grades_lecturer[course] = [grades]
        else:
            print('Ошибка.')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade


class Lecturer(Mentor):

    def average_grade_lectures(self):
        grade_list=[]
        for val in self.dict_grades_lecturer.values():
            grade_list.extend(val)
        sum_=sum(grade_list)
        self.average_grade = round(sum_/len(grade_list),2)
        return self.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\n'\
              f'Средняя оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):

    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            print('Ошибка.')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия = {self.surname}'
        return res
