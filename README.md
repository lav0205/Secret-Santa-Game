# Secret-Santa-Game
<h3>- Background: </h3><br>
Company "Acme" has decided to organize a Secret Santa event among its employees. Each employee is required to choose another employee as their secret child, to whom they will anonymously give a gift during the event. The company wants to automate the process of assigning secret children to employees based on the provided employee information. However, the Secret Santa system has some additional requirements and constraints.

<h3>- Secret Santa Assignment Rules: </h3> <br>
- No Self-Assignments: An employee cannot be assigned to themselves as their Secret Child.<br>
- No Repeated Assignments: If the employee gave a gift to the same person in the previous year, they cannot assign that person again this year.<br>
- Unique Secret Child Assignment: Each employee should have one unique Secret Child, and no one can be assigned the same Secret Child more than once.<br>

# Documentation:
Explanation <br>
1. Employee Class: Each Employee object stores the name, email, and the assigned secret child.<br>
2. SecretSantaGame Class:
    - Loading Employees: The load_employees method loads employee data from a CSV file and stores it in a list of Employee objects.
    - Loading Previous Assignments: The load_previous_assignments method loads the previous year's Secret Santa assignments into a dictionary, where the key is the employee’s name and the value is the name of their       assigned secret child.
    - Assigning Secret Santa: The assign_secret_santa method shuffles the available employees and assigns them secret children according to the rules.
    - Generating Output: The generate_output method writes the assignments into an output CSV file with the required format.
3. Main Function: Reads input files, runs the assignment logic, and writes the result to an output CSV.

Key Features: <br>
- Randomized Assignment: Ensures that each employee is assigned a unique "secret child." <br>
- Excludes Self Assignment: Prevents employees from being their own secret child. <br>
- Avoids Repetition: Ensures that no employee gets the same secret child as last year. <br>
- Error Handling: Basic file handling errors can be extended in a more complex version. <br>
