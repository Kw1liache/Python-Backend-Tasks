from abc import ABC, abstractmethod
from datetime import date


class Printable(ABC):
    @abstractmethod
    def print_info(self) -> None:
        pass


class Book(Printable):
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f"«{self.title}» — {self.author} ({self.year} г.)"

    def print_info(self) -> None:
        print(self.info())

    def __str__(self) -> str:
        return self.info()

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return (
            self.title == other.title
            and self.author == other.author
            and self.year == other.year
        )

    @classmethod
    def from_string(cls, book_str: str) -> "Book":
        title, author, year = book_str.split(";")
        return cls(title.strip(), author.strip(), int(year.strip()))

    @property
    def age(self) -> int:
        return date.today().year - self.year

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 0:
            raise ValueError("Возраст книги не может быть отрицательным!")
        self.year = date.today().year - new_age


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format_type: str) -> None:
        super().__init__(title, author, year)
        self.format_type = format_type

    def info(self) -> str:
        return f"{super().info()}, формат: {self.format_type}"

    @classmethod
    def from_string(cls, book_str: str) -> "Ebook":
        title, author, year, format_type = book_str.split(";")
        return cls(
            title.strip(),
            author.strip(),
            int(year.strip()),
            format_type.strip(),
        )


if __name__ == "__main__":
    book = Book.from_string("Мастер и Маргарита;М.А. Булгаков;1928")
    ebook = Ebook.from_string("Война и мир;Л.Н. Толстой;1869;PDF")

    print(book)
    print(ebook)
    print(f"Возраст книги «{book.title}»: {book.age} лет")
    book.print_info()
    ebook.print_info()
