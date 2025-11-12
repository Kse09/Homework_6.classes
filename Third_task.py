class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'

        if (course in self.courses_in_progress and
                course in lecturer.courses_attached and
                1 <= grade <= 10):

            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)

        average_grade = sum(all_grades) / len(all_grades) if all_grades else 0
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {average_grade:.1f}\n'
               f'Курсы в процессе изучения: {courses_in_progress}\n'
               f'Завершенные курсы: {finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades ={}

    def __str__(self):
        all_lect_grades = []
        for lect_grades in self.grades.values():
            all_lect_grades.extend(lect_grades)

        average_lect_grade = sum(all_lect_grades) / len(all_lect_grades) if all_lect_grades else 0

        return(f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {average_lect_grade:.1f}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and
                course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

# Проверка работы кода
some_reviewer = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy')
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress = ['Python', 'Git']
some_student.finished_courses = ['Введение в программирование']
some_student.grades = {'Python': [10, 9.5, 10]}
some_lecturer.grades = {'Python': [10, 9.5, 10]}

print("====Проверяющие====")
print(some_reviewer)
print("\n====Лекторы====")
print(some_lecturer)
print("\n====Студенты=====")
print(some_student)