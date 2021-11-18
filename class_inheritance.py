#!/usr/bin/env python3

class Person:

    def __init__(self, first_name, last_name, id_number):
        """Constructor for the Person class"""
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def print_person(self):
        """To print an object of the class Person"""
        print("Name of Person: ", self.last_name + ", " + self.first_name)
        print("ID number of the Person: ", self.id_number)


class Student(Person):

    def __init__(self, first_name, last_name, id_number, scores):
        """Constructor for the class Student, which inherits from class Person"""
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number
        self.scores = scores

    def get_grade(self):
        """Method of class Student to calculate and retun grade of an object
        of class Student
        """
        subjects = len(self.scores)

        total_score = 0
        for score in self.scores:
            total_score += score
        average_score = total_score / subjects

        # Assign grade to average_score
        if average_score<=100 and average_score>=90:
            grade = 'O'
        elif average_score<90 and average_score>=80:
            grade = 'E'
        elif average_score<80 and average_score>=70:
            grade = 'A'
        elif average_score<70 and average_score>=55:
            grade = 'P'
        elif average_score<55 and average_score>=40:
            grade = 'D'
        elif average_score < 40:
            grade = 'T'

        return grade
if __name__ == '__main__':

    line = input("Input space separated line containing first name, last name and id number\n").split()
    first_name = line[0]
    last_name = line[1]
    id_num = line[2]

    subjects = int(input("Input number of subjects: "))
    scores = list(map(int, input("Input space separated scores in subjects\n").split()))

    student_1 = Student(first_name, last_name, id_num, scores)
    student_1.print_person()
    print("Grade of student 1: ", student_1.get_grade())
