import sqlalchemy as sqlalchemy
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

#DB_URL = "sqlite:///./dbfile.db"
#engine = sqlalchemy.create_engine(DB_URL, connect_args={"check_same_thread": False})

#DB_URL = "motor://nombre_usuario:password:@urllocalhost:puerto/database_name"
DB_URL = "postgresql://postgres:DVKAnbD7QwnE0fc00PT5@containers-us-west-73.railway.app:6082/railway"
engine = sqlalchemy.create_engine(DB_URL)
SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative.declarative_base()
