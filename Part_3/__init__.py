class Student:
    def __init__(self, name, student_id):
        self._name = name
        self._student_id = student_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            print("Name must be a string")
        else:
            self._name = value

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, int):
            print("Student ID must be an integer")
        else:
            self._student_id = value

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")


class Unit:
    def __init__(self, unit_code, unit_name):
        self._unit_code = unit_code
        self._name = unit_name
        self._students = []

    @property
    def unit_code(self):
        return self._unit_code

    @unit_code.setter
    def unit_code(self, value):
        if not isinstance(value, (str, int)):
            print("Unit code should be a string or an integer.")
        else:
            self._unit_code = value

    @property
    def unit_name(self):
        return self._name

    @unit_name.setter
    def unit_name(self, value):
        if not isinstance(value, str):
            print("Unit name should be a string.")
        else:
            self._name = value

    def add_student(self, student):
        self._students.append(student)

    def remove_student(self, student_id):
        for student in self._students:
            if student.student_id == student_id:
                self._students.remove(student)
                break

    def display_students(self):
        if not self._students:
            print("No students in this unit.")
        else:
            print("Students in the unit:")
            for student in self._students:
                student.display_info()


class Degree:
    def __init__(self, degree_code, name):
        self.degree_code = degree_code
        self.name = name
        self.units = []  

    def add_unit(self, unit):
        self.units.append(unit)

    def remove_unit(self, unit_code):
        for unit in self.units:
            if unit.unit_code == unit_code:
                self.units.remove(unit)
                break

    def display_units(self):
        if not self.units:
            print("No units in this degree.")
        else:
            print("Units in the degree:")
            for unit in self.units:
                print(f"Unit Code: {unit.unit_code}, Name: {unit.unit_name}")



st1 = Student("Dhruv", 1)
st2 = Student("Jackma", 2)
st3 = Student("Joseph", 3)


unit1 = Unit("ISYS1007", "Programmimg 2")
unit2 = Unit("COMP1001", "Data Communication")


degree1 = Degree("063511", "Bachelor of IT")

unit1.add_student(st1)
unit1.add_student(st2)
unit2.add_student(st3)

print("--------------------------------------")

unit1.display_students()
unit2.display_students()

print("--------------------------------------")


unit1.remove_student(1)

print("--------------------------------------")

unit1.display_students()
unit2.display_students()
print("--------------------------------------")


degree1.add_unit(unit1)
degree1.add_unit(unit2)
print("--------------------------------------")


degree1.display_units()
print("--------------------------------------")

degree1.remove_unit("COMP1001")
print("--------------------------------------")

degree1.display_units()