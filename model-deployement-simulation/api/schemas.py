from typing import List, Optional

from pydantic import BaseModel, model_validator


class PredictRequest(BaseModel):
    # Accept either a list of features or named fields
    features: Optional[List[float]] = None
    sepal_length: Optional[float] = None
    sepal_width: Optional[float] = None
    petal_length: Optional[float] = None
    petal_width: Optional[float] = None

    @model_validator(mode="before")
    def build_features(cls, values):
        # values is the raw input mapping
        feats = values.get("features")
        if feats is not None:
            if not isinstance(feats, (list, tuple)) or len(feats) != 4:
                raise ValueError("features must be a list of length 4")
            values["features"] = [float(x) for x in feats]
            return values

        named = (
            values.get("sepal_length"),
            values.get("sepal_width"),
            values.get("petal_length"),
            values.get("petal_width"),
        )
        if all(v is not None for v in named):
            values["features"] = [float(v) for v in named]
            return values

        raise ValueError(
            "Provide either 'features' (length 4) or all named fields: sepal_length, sepal_width, petal_length, petal_width"
        )