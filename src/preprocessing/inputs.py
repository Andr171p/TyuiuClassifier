import numpy as np
import pandas as pd
from pydantic import BaseModel
from typing import Any, Dict, List


class Inputs:
    def __init__(
            self,
            inputs: BaseModel,
            features: List[str]
    ) -> None:
        self._inputs = inputs.model_dump()
        self._data: Dict[str, Any] = {feature: 0 for feature in features}

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(
            data=self._data,
            index=[0]
        )
    
    def fill_values(self) -> None:
        self._data['Пол'] = self._inputs['gender']
        self._data['Нуждается в общежитии'] = self._inputs['hostel']
        self._data['Приоритет'] = self._inputs['priority']
        self._data['Сумма баллов'] = self._inputs['exams_points']
        self._data['Сумма баллов за индивидуальные достижения'] = self._inputs['bonus_points']
        self._data[f'Полученное образование_{self._inputs['education']}'] = True
        self._data[f'Форма обучения_{self._inputs['study_form']}'] = True
        self._data[f'Вид приема_{self._inputs['reception_form']}'] = True
        self._data[f'Направление подготовки_{self._inputs['speciality']}'] = True
