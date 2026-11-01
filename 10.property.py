class Student:
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value

    @property
    def grade(self):
        if self._score >= 90:
            return "A"
        elif self._score >= 60:
            return "B"
        else:
            return "C"


s = Student()
s.score = 90
print(s.score)
print(s.grade)
# s.grade = "B"  # AttributeError: property 'grade' of 'Student' object has no setter
