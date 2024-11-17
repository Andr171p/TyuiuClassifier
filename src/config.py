from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR: Path = Path(__file__).resolve().parent.parent


class DataSettings(BaseSettings):
    features_path: str = BASE_DIR / "data" / "columns.csv"


class ModelSettings(BaseSettings):
    model_path: str = BASE_DIR / "models" / "random-forrest-model.joblib"


class Settings(BaseSettings):
    data: DataSettings = DataSettings()
    model: ModelSettings = ModelSettings()


settings = Settings()
