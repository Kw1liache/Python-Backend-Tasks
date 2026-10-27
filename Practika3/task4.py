class SpaceShip:
    def __init__(
        self,
        name: str,
        fuel: float,
        hull_condition: int = 100,
        speed: float = 0,
    ) -> None:
        if fuel < 0:
            raise ValueError("Запас топлива не может быть отрицательным.")
        if not 0 <= hull_condition <= 100:
            raise ValueError("Состояние корпуса должно быть от 0 до 100.")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной.")
        self.name = name
        self.fuel = fuel
        self.hull_condition = hull_condition
        self.speed = speed

    def travel(self, distance: float) -> None:
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным.")
        fuel_needed = distance * 0.1
        if fuel_needed > self.fuel:
            raise ValueError("Недостаточно топлива для полёта.")
        self.fuel -= fuel_needed

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("Урон не может быть отрицательным.")
        self.hull_condition = max(0, self.hull_condition - damage)


class CrewMember:
    def __init__(
        self, name: str, role: str, health: int = 100, skills: list[str] | None = None
    ) -> None:
        if not 0 <= health <= 100:
            raise ValueError("Здоровье должно быть от 0 до 100.")
        self.name = name
        self.role = role
        self.health = health
        self.skills = skills or []


class Mission:
    def __init__(
        self,
        name: str,
        goals: list[str],
        resources: dict[str, int],
        possible_events: list[str],
    ) -> None:
        self.name = name
        self.goals = goals
        self.resources = resources
        self.possible_events = possible_events
        self.events: list[str] = []

    def record_event(self, event: str) -> None:
        if event not in self.possible_events:
            raise ValueError("Такое событие не предусмотрено миссией.")
        self.events.append(event)


if __name__ == "__main__":
    ship = SpaceShip("Одиссей", fuel=500, speed=1200)
    crew = [
        CrewMember("Елена", "пилот", skills=["навигация", "пилотирование"]),
        CrewMember("Олег", "инженер", skills=["ремонт", "робототехника"]),
    ]
    mission = Mission(
        "Экспедиция к Марсу",
        goals=["Исследовать поверхность", "Собрать образцы"],
        resources={"еда": 30, "медицинские наборы": 5},
        possible_events=["Встреча с астероидом", "Поломка двигателя"],
    )

    ship.travel(100)
    mission.record_event("Встреча с астероидом")
    ship.take_damage(10)

    print(f"Миссия: {mission.name}")
    print(f"Цели: {', '.join(mission.goals)}")
    print(f"Экипаж: {', '.join(member.name for member in crew)}")
    print(f"Топливо: {ship.fuel:.1f}, корпус: {ship.hull_condition}%")
    print(f"События: {', '.join(mission.events)}")
