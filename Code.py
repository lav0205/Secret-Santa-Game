import csv
import random

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.secret_child = None

class SecretSantaGame:
    def __init__(self, employees_file, previous_assignments_file):
        self.employees = self.load_employees(employees_file)
        self.previous_assignments = self.load_previous_assignments(previous_assignments_file)
        self.assignments = {}

    def load_employees(self, employees_file):
        employees = []
        try:
            with open(employees_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
        except Exception as e:
            print(f"Error reading employees file: {e}")
        return employees

    def load_previous_assignments(self, previous_assignments_file):
        assignments = {}
        try:
            with open(previous_assignments_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    assignments[row['Employee_Name']] = row['Secret_Child_Name']
        except Exception as e:
            print(f"Error reading previous assignments file: {e}")
        return assignments

    def assign_secret_santa(self):
        available_santas = self.employees[:]
        random.shuffle(available_santas)
        employees_dict = {e.name: e for e in self.employees}
        for employee in self.employees:
            for potential_child in available_santas:
                if potential_child.name != employee.name and \
                   (employee.name not in self.previous_assignments or self.previous_assignments[employee.name] != potential_child.name):
                    employee.secret_child = potential_child
                    available_santas.remove(potential_child)
                    break

    def generate_output(self, output_file):
        try:
            with open(output_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'])
                writer.writeheader()

                for employee in self.employees:
                    writer.writerow({
                        'Employee_Name': employee.name,
                        'Employee_EmailID': employee.email,
                        'Secret_Child_Name': employee.secret_child.name,
                        'Secret_Child_EmailID': employee.secret_child.email
                    })
        except Exception as e:
            print(f"Error writing output file: {e}")

def main():
    employees_file = 'employees.csv'
    previous_assignments_file = 'previous_assignment.csv'
    output_file = 'secret_santa_assignments.csv'

    game = SecretSantaGame(employees_file, previous_assignments_file)
    game.assign_secret_santa()
    game.generate_output(output_file)
    print(f"Secret Santa assignments have been written to {output_file}")

if __name__ == "__main__":
    main()
