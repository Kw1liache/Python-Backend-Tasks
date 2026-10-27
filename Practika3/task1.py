class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def calculate_salary(self) -> float:
        return self.salary

    def salary_increase(self, percent: float) -> None:
        if percent < 0:
            raise ValueError("Процент повышения не может быть отрицательным.")
        self.salary += self.salary * percent / 100


class Manager(Employee):
    def __init__(
        self, name: str, salary: float, department: str, bonus_percent: float = 0
    ) -> None:
        super().__init__(name, salary)
        self.department = department
        self.bonus_percent = bonus_percent

    def calculate_salary(self) -> float:
        return self.salary * (1 + self.bonus_percent / 100)


class Developer(Employee):
    def __init__(
        self,
        name: str,
        salary: float,
        programming_language: str,
        completed_projects: int = 0,
        project_bonus: float = 0,
    ) -> None:
        super().__init__(name, salary)
        self.programming_language = programming_language
        self.completed_projects = completed_projects
        self.project_bonus = project_bonus

    def calculate_salary(self) -> float:
        return self.salary + self.completed_projects * self.project_bonus


if __name__ == "__main__":
    employee = Employee("Анна", 50000)
    manager = Manager("Иван", 70000, "Продажи", bonus_percent=20)
    developer = Developer(
        "Мария", 80000, "Python", completed_projects=3, project_bonus=5000
    )

    for person in (employee, manager, developer):
        print(f"{person.name}: зарплата {person.calculate_salary():.2f} руб.")

    employee.salary_increase(10)
    print(f"После повышения зарплата Анны: {employee.calculate_salary():.2f} руб.")
