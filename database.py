from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL Database URL (Replace 'yourusername', 'yourpassword', 'yourdatabase' with actual values)
DATABASE_URL = "postgresql+psycopg2://postgres:happysql@localhost:5432/RestapiDB"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session for interacting with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for models
Base = declarative_base()
