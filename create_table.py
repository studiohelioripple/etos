from app_kernel.db import engine, Base
from app_kernel.models import User

Base.metadata.create_all(bind=engine)
print("Tables created.")
