import sqlalchemy as db

from .base_model import Base


class Tag(Base):
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False, unique=True)


class LinkCourseTag(Base):
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

