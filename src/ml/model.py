import joblib
from typing import Any, Optional
from sklearn.ensemble import RandomForestClassifier

from src.config import settings


class BinaryClassifierModel:
    def __init__(self) -> None:
        self._model: Optional[RandomForestClassifier] = None

    def load(
            self,
            path: str = settings.model.model_path
    ) -> RandomForestClassifier | None:
        self._model = joblib.load(path)
        return self._model
    
    def predict(self, x: Any) -> Any:
        return self._model.predict(x)[0]
    
    def predict_proba(self, x: Any) -> Any:
        return self._model.predict_proba(x)[0]
