"""
Project configuration for Philippine Crop Production and Climate Risk Lakehouse.

Catalog/schema names, volume paths, table names, and shared constants
used across Bronze → Silver → Gold → ML notebooks.
"""

from dataclasses import dataclass

# ---------------------------------------------------------------------------
# Unity Catalog & Volume
# ---------------------------------------------------------------------------
CATALOG = 'crop_medallion_architecture'

SCHEMAS = {
    'bronze': 'bronze',
    'silver': 'silver',
    'gold': 'gold',
    'ml': 'ml',
    'source_data': 'source_data'
}

VOLUME_SCHEMA = 'source_data'
VOLUME_NAME = 'raw'
VOLUME_PATH = f'/Volumes/{CATALOG}/{VOLUME_SCHEMA}/{VOLUME_NAME}'

SOURCE_FILES = {
    'crop_trend': 'crop_trend.csv',
    'weather': 'province_weather_quarterly.csv'
}


# ---------------------------------------------------------------------------
# Fully-qualified table names
# ---------------------------------------------------------------------------
def fq(schema: str, table: str) -> str:
    return f'{CATALOG}.{schema}.{table}'

BRONZE_TABLES = {
    'crop_production_raw': fq('bronze', 'crop_production_raw'),
    'weather_raw': fq('bronze', 'weather_raw')
}

SILVER_TABLES = {
    'crop_production_clean': fq('silver', 'crop_production_clean'),
    'weather_clean': fq('silver', 'weather_clean'),
    'province_mapping': fq('silver', 'province_mapping'),
    'crop_production_enriched': fq('silver', 'crop_production_enriched')
}

GOLD_TABLES = {
    'province_quarter_summary': fq('gold', 'province_quarter_summary'),
    'crop_group_trends': fq('gold', 'crop_group_trends'),
    'crop_province_performance': fq('gold', 'crop_province_performance'),
    'ml_crop_forecast_features': fq('gold', 'ml_crop_forecast_features'),
    'data_quality_metrics': fq('gold', 'data_quality_metrics')
}

ML_TABLES = {
    'crop_production_predictions': fq('ml', 'crop_production_predictions')
}

MODEL_NAME = f'{CATALOG}.ml.crop_production_forecaster'


# ---------------------------------------------------------------------------
# Business constants
# ---------------------------------------------------------------------------
BUSINESS_KEY_COLS = ['province', 'crop', 'year', 'quarter']
VALID_QUARTERS = ['Q1', 'Q2', 'Q3', 'Q4']
CROP_GROUPS = ['PALAY', 'CORN', 'OTHER']
RISK_LABELS = ['Stable', 'Risk-prone', 'High', 'Declining']

# ML chronological split
TRAIN_END_YEAR = 2022
VALIDATION_YEARS = [2023, 2024]
TEST_YEAR = 2025

@dataclass
class ProjectPaths:
    volume_path: str = VOLUME_PATH
    crop_csv: str = f'{VOLUME_PATH}/{SOURCE_FILES['crop_trend']}'
    weather_csv: str = f'{VOLUME_PATH}/{SOURCE_FILES['weather']}'

PATHS = ProjectPaths()