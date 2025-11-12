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

    def get_avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()


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

    def get_avg_grade(self):
        all_grades = []
        for course_grades in self.grades.values():
            all_grades.extend(course_grades)
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __gt__(self, other):
        return self.get_avg_grade() > other.get_avg_grade()

    def __lt__(self, other):
        return self.get_avg_grade() < other.get_avg_grade()

    def __eq__(self, other):
        return self.get_avg_grade() == other.get_avg_grade()


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

# Подсчет средней оценки студентов по курсу
def avg_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])

    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0

# Подсчет средней оценки лекторов по курсу
def avg_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])

    if total_grades:
        return sum(total_grades) / len(total_grades)
    else:
        return 0

# Проверка работы кода
# Создаем двух студентов
student1 = Student('Иван', 'Иванов', 'М')
student1.courses_in_progress = ['Python', 'Git']
student1.finished_courses = ['Введение в программирование']
student2 = Student('Мария', 'Петрова', 'Ж')
student2.courses_in_progress = ['Python', 'Git', 'ООП и работа с API']
student2.finished_courses = ['Основы программирования']

# Создаем двух лекторов
lecturer1 = Lecturer('Алексей', 'Сидоров')
lecturer1.courses_attached = ['Python', 'Git']
lecturer2 = Lecturer('Ольга', 'Кузнецова')
lecturer2.courses_attached = ['Python', 'ООП и работа с API']

# Создаем двух проверяющих
reviewer1 = Reviewer('Дмитрий', 'Смирнов')
reviewer1.courses_attached = ['Python', 'Git']
reviewer2 = Reviewer('Елена', 'Васильева')
reviewer2.courses_attached = ['SQL', 'Git']

# Проверяющие выставляют оценки студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student2, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Git', 8)
reviewer2.rate_hw(student2, 'ООП и работа с API', 9)

# Студенты оценивают лекторов
student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Git', 9)
student2.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer2, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'ООП и работа с API', 8)

# Проверка метода __str__
print("=== Информация о проверяющих ===")
print(reviewer1)
print()
print(reviewer2)
print("\n=== Информация о лекторах ===")
print(lecturer1)
print()
print(lecturer2)
print("\n=== Информация о студентах ===")
print(student1)
print()
print(student2)

# Проверка методов сравнения по средней оценке
print("\n=== Сравнение студентов по средним оценкам ===")
print(f"student1 > student2: {student1 > student2}")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 == student2: {student1 == student2}")
print("\n=== Сравнение лекторов по средним оценкам ===")
print(f"lecturer1 > lecturer2: {lecturer1 > lecturer2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")

# Проверка подсчета средних оценок по домашним заданиям и лекциям
print("\n=== Средние оценки по курсам ===")
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
python_avg_hw = avg_hw_grade(students_list, 'Python')
git_avg_hw = avg_hw_grade(students_list, 'Git')
sql_avg_hw = avg_hw_grade(students_list, 'ООП и работа с API')
python_avg_lecture = avg_lecture_grade(lecturers_list, 'Python')
git_avg_lecture = avg_lecture_grade(lecturers_list, 'Git')
sql_avg_lecture = avg_lecture_grade(lecturers_list, 'ООП и работа с API')

print(f"Средняя оценка за домашние задания по Python: {python_avg_hw:.1f}")
print(f"Средняя оценка за домашние задания по Git: {git_avg_hw:.1f}")
print(f"Средняя оценка за домашние задания по ООП и работа с API: {sql_avg_hw:.1f}")
print(f"Средняя оценка за лекции по Python: {python_avg_lecture:.1f}")
print(f"Средняя оценка за лекции по Git: {git_avg_lecture:.1f}")
print(f"Средняя оценка за лекции по ООП и работа с API: {sql_avg_lecture:.1f}")