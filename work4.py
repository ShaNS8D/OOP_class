class Mentor:

    mentor_list = []
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.dict_grades_lecturer = {}
        self.average_grade = 0
        self.mentor_list.append(self)

class Student:

    student_list = []
    def __init__(self,name,surname,gender,):
        self.name=name
        self.surname = surname
        self.gender=gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_dict_student = {}
        self.average_grade = 0
        self.student_list.append(self)

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


reviewer_1 = Reviewer ('Иван','Иванов')
print(reviewer_1)                        
                                         
lecturer_1 = Lecturer('Егор','Егоров')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Анна','Петрова')
lecturer_2.courses_attached.append('Python')

student_1= Student('Вася','Теркин','мужик')
student_1.courses_in_progress.append('Python')
student_2= Student('Надя','Жукова','мадама')
student_2.courses_in_progress.append('Python')
student_3= Student('Елена','Гурнак','мадама')
student_3.courses_in_progress.append('Python')
student_4 = Student('Петр','Ершов','мужик')
student_4.courses_in_progress.append('WEB')
student_5 = Student('Вера','Сивова','мадама')
student_5.courses_in_progress.append('WEB')

student_1.scoring_method(lecturer_1, 'Python', 9)
student_2.scoring_method(lecturer_1, 'Python', 9)
student_3.scoring_method(lecturer_1, 'Python', 10)

student_1.scoring_method(lecturer_2, 'Python', 9)
student_2.scoring_method(lecturer_2, 'Python', 8)
student_3.scoring_method(lecturer_2, 'Python', 8)

print(lecturer_1.dict_grades_lecturer)
print(lecturer_2.dict_grades_lecturer) 
print(lecturer_1.average_grade_lectures()) 
print(lecturer_1)

reviewer_1 = Reviewer ('Иван','Иванов')
reviewer_1.courses_attached.append('Python')
reviewer_1.courses_attached.append('WEB')
reviewer_1.add_grades_student(student_1, 'Python', 10) 
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)
print(f'Оценки для student_1 - {student_1.grades_dict_student }')
reviewer_1.add_grades_student(student_2, 'Python', 8)
reviewer_1.add_grades_student(student_2, 'Python', 9)
reviewer_1.add_grades_student(student_2, 'Python', 9)
print(f'Оценки для student_2 - {student_2.grades_dict_student }')
reviewer_1.add_grades_student(student_3, 'Python', 8)
reviewer_1.add_grades_student(student_3, 'Python', 9)
reviewer_1.add_grades_student(student_3, 'Python', 8)
print(f'Оценки для student_3 - {student_3.grades_dict_student }')

reviewer_1.add_grades_student(student_4, 'WEB', 8)
reviewer_1.add_grades_student(student_4, 'WEB', 7)
reviewer_1.add_grades_student(student_4, 'WEB', 8)
print(f'Оценки для student_4 - {student_4.grades_dict_student }')

reviewer_1.add_grades_student(student_5, 'WEB', 6)
reviewer_1.add_grades_student(student_5, 'WEB', 8)
reviewer_1.add_grades_student(student_5, 'WEB', 6)
print(f'Оценки для student_5 - {student_5.grades_dict_student }')
print(student_1.average_grade_student()) 

student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)

student_1.finished_courses.append('Введение в программирование')
print(student_1)

print (lecturer_1.dict_grades_lecturer)
print (lecturer_2.dict_grades_lecturer)

lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()
print(lecturer_1.average_grade,lecturer_2.average_grade)
print(lecturer_1 < lecturer_2) 

student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()
print(student_1.average_grade,student_2.average_grade)
print(student_1 > student_2) 

def get_average_grade_student_course (other_list,course):
    all_grades_list_course = []
    for student in other_list:
        for key, value in student.grades_dict_student.items():
            if key == course:
                all_grades_list_course.extend(value)
    sum_ = sum(all_grades_list_course)
    average_grade_student = round(sum_ / len(all_grades_list_course), 2)
    return average_grade_student

print(get_average_grade_student_course (Student.student_list,"Python"))
print(get_average_grade_student_course (Student.student_list,'WEB'))

def get_lecturer_course(other_list):
    lecturer_course_all = []
    for mentor in other_list:
        if len(mentor.dict_grades_lecturer) > 0:
            lecturer_course_all.extend(mentor.courses_attached)
    lecturer_course_list = list(set(lecturer_course_all))
    return lecturer_course_list

print(get_lecturer_course(Mentor.mentor_list))

def get_average_grade_mentor_course (other_list,course):
    lecturer_course_list = get_lecturer_course(other_list)
    if course not in lecturer_course_list :
        print('Ошибка.Такого курса нет в списке курсов лекторов')
        return
    all_grades_lecturer_course = []
    for lecturer in other_list:
        if len(lecturer.dict_grades_lecturer) > 0:
            for key, value in lecturer.dict_grades_lecturer.items():
                if key == course:
                    all_grades_lecturer_course.extend(value) 
    sum_ = sum(all_grades_lecturer_course)
    average_grade_lecturer = round(sum_ / len(all_grades_lecturer_course), 2)
    return average_grade_lecturer

print(get_average_grade_mentor_course(Mentor.mentor_list,'Python'))
print(get_average_grade_mentor_course(Mentor.mentor_list,'ython'))






