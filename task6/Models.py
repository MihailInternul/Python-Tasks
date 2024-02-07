from typing import List


class Survey:
    title: str
    pages: List["Page"]

class Page:
    title: str
    questions: List["Question"]

class Question:
    title: str
    answers: List[str]
    description: str

