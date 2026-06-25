# oop_practice.py

# ==========================================
# 1. STUDENT CLASS (OOP & Encapsulation)
# ==========================================
class Student:
    def __init__(self, name, degree, role):
        self.name = name
        self.degree = degree
        self.role = role
        # The underscore means this is a "private" variable (Encapsulation)
        self._grades = [] 

    def add_grade(self, grade):
        """Method to safely add a grade with validation"""
        if 0 <= grade <= 100:
            self._grades.append(grade)
            print(f"Successfully added grade {grade} for {self.name}.")
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def get_average(self):
        """Calculates the student's average grade"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

# ==========================================
# 2. CALCULATOR (Exception Handling)
# ==========================================
class Calculator:
    def divide(self, a, b):
        """Divides two numbers with strict error handling"""
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Server Error: You cannot divide by zero!"
        except TypeError:
            return "Server Error: Please provide numbers, not text."

# ==========================================
# 3. TESTING THE CODE (Creating Objects)
# ==========================================
if __name__ == "__main__":
    print("--- TESTING STUDENT MODULE ---")
    # Creating an object using your info!
    intern = Student("Amal", "MCA", "Django Developer Intern")
    
    intern.add_grade(95)
    intern.add_grade(88)
    print(f"{intern.name}'s Average Score: {intern.get_average()}")

    print("\n--- TESTING CALCULATOR MODULE ---")
    calc = Calculator()
    
    print(f"10 / 2 = {calc.divide(10, 2)}")
    # This will trigger our exception handling instead of crashing!
    print(f"10 / 0 = {calc.divide(10, 0)}")