import os

class Settings:
    PROJECT_NAME = "Country API"
    PROJECT_VERSION = "1.0.0"
    
    # Database settings from Kubernetes ConfigMap and Secret
    # These environment variables serán configuradas por Kubernetes
    # usando ConfigMap y Secret
    MYSQL_USER = os.getenv("MYSQL_USER")  # from ConfigMap
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")  # from Secret
    MYSQL_HOST = os.getenv("MYSQL_HOST")  # from ConfigMap
    MYSQL_PORT = os.getenv("MYSQL_PORT")  # from ConfigMap
    MYSQL_DB = os.getenv("MYSQL_DB")  # from ConfigMap
    
    @property
    def DATABASE_URL(self):
        return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}"

settings = Settings()