from sqlalchemy import MetaData, create_engine

from src.config import get_settings

settings = get_settings()

DB_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

engine = create_engine(settings.DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)