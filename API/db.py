from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from databases import Database

SQLALCHEMY_DATABASE_URL = "mysql://root:islam@localhost/hotel"

database = Database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)# echo=True permet d'afficher les requêtes SQL générées par SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)# la fonction sessionmaker est définie dans sqlalchemy.orm
Base = declarative_base(metadata=MetaData())# la fonction declarative_base est définie dans sqlalchemy.ext.declarative
