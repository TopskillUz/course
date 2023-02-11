import re
import datetime

import sqlalchemy as db
from sqlalchemy import types
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy.orm.query
import sqlalchemy.event
from typing import Set, Optional, Any

from core.config import settings


def camelcase_to_snakecase(name: str) -> str:
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    return pattern.sub('_', name).lower()


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return camelcase_to_snakecase(cls.__name__)

    # __table_args__ = {'mysql_engine': 'InnoDB'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column('created_at', db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column('updated_at', db.DateTime, onupdate=datetime.datetime.now)
    deleted_at = db.Column(db.DateTime, default=None)


Base = declarative_base(cls=Base)


# @db.event.listens_for(db.orm.Mapper, 'refresh', named=True)
# def on_instance_refresh(target: type,
#                         context: db.orm.query.QueryContext,
#                         attrs: Optional[Set[str]]):
#     ssn: sqlalchemy.orm.Session = context.session
#     # target.deleted_at = datetime.datetime.now
#     print(38, target.id, attrs)
#     return target


class SaTranslationFieldComparator(JSONB.Comparator):
    def __eq__(self, other: Any) -> bool:
        default = settings.ALLOWED_LANGUAGES[0]
        return self.contains({default: other})


class SaTranslationField(types.TypeDecorator):
    impl: JSONB = JSONB()
    cache_ok = True
    comparator_factory = SaTranslationFieldComparator

    def coerce_compared_value(self, op: Any, value: Any) -> types.TypeEngine[Any]:
        return self.impl.coerce_compared_value(op, value)

    def process_bind_param(self, value: Any, dialect: Any) -> Optional[dict]:  # type: ignore
        if isinstance(value, dict):
            if not all(map(lambda k: k in settings.ALLOWED_LANGUAGES, value.keys())):
                raise ValueError("This language cannot be added to the database")
            return value
        elif isinstance(value, str):
            default = settings.ALLOWED_LANGUAGES[0]
            return {default: value}
        return dict()

    def process_result_value(self, value: Any, dialect: Any) -> Optional[Any]:
        # translated = value.get("uz")
        return value


def TranslationField(**kwargs: Any) -> Any:
    return db.Column(SaTranslationField, nullable=False, default=dict(), **kwargs)

# q = select(Region).filter(
#            Region.title['uz'].astext.cast(String) == "Toshkent"
#        )
