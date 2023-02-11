import enum

import sqlalchemy as db
from sqlalchemy import Enum, event
from sqlalchemy.dialects import postgresql

from .base_model import Base, TranslationField


class BaseCourseModel(Base):
    __abstract__ = True

    title = TranslationField()
    desc = TranslationField()
    is_active = db.Column(db.Boolean, default=True)
    sort = db.Column(db.Integer, default=1)
    slug = db.Column(db.String, nullable=False, unique=True)


@event.listens_for(BaseCourseModel, 'before_insert')
def base_course_model_before_insert(mapper, connect, target):
    print(mapper, connect, target)


class Profession(BaseCourseModel):
    """ Kasblar:
            1. Dasturlash
            2. Dizayn
            3. Marketing
            4. Analitika
    """


class Topic(BaseCourseModel):
    profession_id = db.Column(db.Integer, db.ForeignKey("profession.id"))


class Category(BaseCourseModel):
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"))
    logo_id = db.Column(db.Integer)  # fk(image_media)


class CourseStatusEnum(int, enum.Enum):
    public = 0
    private = 1
    premiere = 2


class DifficultyLevelEnum(int, enum.Enum):
    beginner = 0
    intermediate = 1
    expert = 2


class LanguageEnum(int, enum.Enum):
    uz = 0
    ru = 1
    en = 2


class Course(BaseCourseModel):
    sub_title = TranslationField()
    created_by = db.Column(db.Integer, nullable=False)  # fk(user)
    price = db.Column(db.Float, default=0)
    is_free = db.Column(db.Boolean, default=False)
    banner_image = db.Column(db.Integer, nullable=True)  # fk(image_media)
    trailer = db.Column(db.Integer, nullable=True)  # fk(file_media)
    organization_id = db.Column(db.Integer, nullable=True)  # fk(organization)
    status = db.Column(Enum(CourseStatusEnum), default=CourseStatusEnum.public)
    is_verified = db.Column(db.Boolean, default=False)
    is_for_child = db.Column(db.Boolean, default=False)
    level = db.Column(Enum(DifficultyLevelEnum), default=DifficultyLevelEnum.beginner)
    language = db.Column(Enum(LanguageEnum), default=LanguageEnum.uz)
    installment_payment_id = db.Column(db.Integer, nullable=True)  # fk(installment_payment)
    discount_id = db.Column(db.Integer, nullable=True)  # fk(discount)


class LinkCategoryCourse(Base):
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)


class CourseModule(BaseCourseModel):
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    content = TranslationField()
    is_free = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float, default=0)
    level = db.Column(postgresql.ENUM(DifficultyLevelEnum, create_type=False, checkfirst=True,
                                      inherit_schema=True), default=DifficultyLevelEnum.beginner)
    discount_id = db.Column(db.Integer, nullable=True)  # fk(discount)


class CourseLesson(BaseCourseModel):
    course_module_id = db.Column(db.Integer, db.ForeignKey('course_module.id'))
    content = TranslationField()
    is_free = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float, default=0)
    video_id = db.Column(db.Integer, nullable=True)  # fk(file_media)
    is_learned = db.Column(db.Boolean, default=False)
    discount_id = db.Column(db.Integer, nullable=True)  # fk(discount)


class CourseComment(Base):
    created_by = db.Column(db.Integer, nullable=False)  # fk(user)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    replied_by = db.Column(db.Integer, db.ForeignKey('course_comment.id'))


class LinkUserAllowedCourse(Base):
    user_id = db.Column(db.Integer, nullable=False)  # fk(user)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)


class LinkUserAllowedCourseModule(Base):
    user_id = db.Column(db.Integer, nullable=False)  # fk(user)
    course_module_id = db.Column(db.Integer, db.ForeignKey("course_module.id"), nullable=False)


class LinkUserAllowedCourseLesson(Base):
    user_id = db.Column(db.Integer, nullable=False)  # fk(user)
    course_lesson_id = db.Column(db.Integer, db.ForeignKey("course_lesson.id"), nullable=False)
