"""
ETL configuration (Setup -> Bronze -> Silver -> Gold).
Catalog, schema and table names, source file paths, and the business rules used by the ETL notebooks.
"""

CATALOG = "ph_crop_climate"

# ---------------------------------------------------------------------------
# Schemas and the volume that holds the source CSV files
# ---------------------------------------------------------------------------
SOURCE_VOLUME_SCHEMA = "landing"
SOURCE_VOLUME_NAME = "source_files"
SOURCE_VOLUME_PATH = f"/Volumes/{CATALOG}/{SOURCE_VOLUME_SCHEMA}/{SOURCE_VOLUME_NAME}"

SCHEMAS_TO_CREATE = [SOURCE_VOLUME_SCHEMA, "bronze", "silver", "gold", "ml"]

CROP_FILE_NAME = "crop_trend.csv"
WEATHER_FILE_NAME = "province_weather_quarterly.csv"
CROP_CSV_PATH = f"{SOURCE_VOLUME_PATH}/{CROP_FILE_NAME}"
WEATHER_CSV_PATH = f"{SOURCE_VOLUME_PATH}/{WEATHER_FILE_NAME}"

# ---------------------------------------------------------------------------
# Tables (catalog.schema.table)
# ---------------------------------------------------------------------------
BRONZE_CROP_TABLE = f"{CATALOG}.bronze.crop_production"
BRONZE_WEATHER_TABLE = f"{CATALOG}.bronze.weather"

SILVER_CROP_TABLE = f"{CATALOG}.silver.crop_production"
SILVER_WEATHER_TABLE = f"{CATALOG}.silver.weather"
SILVER_CROP_WEATHER_TABLE = f"{CATALOG}.silver.crop_production_weather"

GOLD_PROVINCE_SUMMARY_TABLE = f"{CATALOG}.gold.province_quarter_summary"
GOLD_CROP_GROUP_TRENDS_TABLE = f"{CATALOG}.gold.crop_group_trends"
GOLD_CROP_PERFORMANCE_TABLE = f"{CATALOG}.gold.crop_province_performance"
GOLD_FORECAST_FEATURES_TABLE = f"{CATALOG}.gold.crop_forecast_features"
GOLD_QUALITY_METRICS_TABLE = f"{CATALOG}.gold.data_quality_metrics"

# ---------------------------------------------------------------------------
# Business rules
# ---------------------------------------------------------------------------
# One crop row = one province + crop + year + quarter
CROP_KEY_COLUMNS = ["province", "crop", "year", "quarter"]
VALID_QUARTERS = ["Q1", "Q2", "Q3", "Q4"]
VALID_CROP_GROUPS = ["PALAY", "CORN", "OTHER"]