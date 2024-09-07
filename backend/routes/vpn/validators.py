from enum import Enum

from pydantic import BaseModel, EmailStr


class BookCourseValidator(BaseModel):
    email: EmailStr
    username: str
    password: str
    fuel: str
    courses: list

    def packing_data(self) -> list[tuple[str, str]]:
        return [(course.course_name, course.course_id) for course in self.courses]


class CourseValidator(BaseModel):
    course_id: str
    course_name: str
    jxb_id: str
    jxbmc: str


class PEValidator(CourseValidator):
    grade: int


class PCValidator(CourseValidator):
    pass


class BookPEValidator(BookCourseValidator):
    courses: list[PEValidator]


class BookPCValidator(BookCourseValidator):
    courses: list[PCValidator]


class CourseTypeEnum(Enum):
    pc = '10'
    pe = '05'
