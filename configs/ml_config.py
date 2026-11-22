"""
ML configuration (train -> evaluate -> batch inference).
The ML notebooks read the Gold feature table and write predictions to the `ml` schema.
"""

from configs.etl_config import CATALOG, GOLD_FORECAST_FEATURES_TABLE

# ---------------------------------------------------------------------------
# Input / output
# ---------------------------------------------------------------------------
FEATURE_TABLE = GOLD_FORECAST_FEATURES_TABLE

PREDICTIONS_TABLE = f"{CATALOG}.ml.crop_production_predictions"

# The trained model is stored in the Unity Catalog Model Registry: catalog.schema.model
MODEL_NAME = "crop_production_forecaster"
REGISTERED_MODEL_NAME = f"{CATALOG}.ml.{MODEL_NAME}"
MODEL_ALIAS = "champion"   # the version that evaluation, batch inference and serving use

# ---------------------------------------------------------------------------
# Chronological split (never shuffle time-series data)
# ---------------------------------------------------------------------------
TRAIN_END_YEAR = 2022
VALIDATION_YEARS = [2023, 2024]
TEST_YEAR = 2025

# ---------------------------------------------------------------------------
# Features and label
# ---------------------------------------------------------------------------
LABEL_COLUMN = "production_next_quarter"

# growth_rate_yoy and risk_label are NOT features: they describe the same quarter
# as the label and would leak the answer into the model.
# production_year_ago is also not a feature: it is only used for the predicted YoY in batch inference.
NUMERIC_FEATURES = [
    "production_lag_1", "production_lag_2", "production_lag_3", "production_lag_4",
    "quarter_num",
    "temperature_2m_mean", "temperature_2m_max", "temperature_2m_min",
    "precipitation_sum", "rain_sum", "precipitation_hours",
    "sunshine_duration", "reference_evapotranspiration_mm",
    "wind_speed_10m_max", "wind_gusts_10m_max",
    "rainfall_deviation_pct", "temperature_anomaly_c",
    "temp_anomaly_rolling", "rain_anomaly_rolling",
    "oni_index",
]
BOOLEAN_FEATURES = ["enso_phase_la_nina", "enso_phase_neutral"]
CATEGORICAL_FEATURES = ["province", "crop", "crop_group"]
ALL_FEATURE_COLUMNS = NUMERIC_FEATURES + BOOLEAN_FEATURES + CATEGORICAL_FEATURES

# ---------------------------------------------------------------------------
# Predicted risk rules (used by batch inference)
# ---------------------------------------------------------------------------
DECLINE_THRESHOLD = -0.2         # predicted YoY growth at or below this -> "Declining"
GROWTH_THRESHOLD = 0.2           # predicted YoY growth at or above this -> "High"
CLIMATE_STRESS_THRESHOLD = 30.0  # climate stress at or above this -> "Risk-prone"