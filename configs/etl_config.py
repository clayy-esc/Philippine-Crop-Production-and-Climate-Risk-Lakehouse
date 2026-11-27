"""

ETL configuration (setup -> bronze -> silver -> gold)
- Catalog, schema and table names, source file paths, and the business rules used by the ETL notebooks.

Unity Catalog naming convention (all lowercase snake_case):
    catalog                 ph_crop_climate
    schema                  landing, bronze, silver, gold, ml
    table                   
    volume                  landing.source_files
    
"""

CATALOG = 'ph_crop_climate'
SCHEMAS = ['landing', 'bronze', 'silver', 'gold', 'ml']

SOURCE_VOLUME_SCHEMA = 'landing'
SOURCE_VOLUME_NAME = 'source_files'
SOURCE_VOLUME_PATH = f'/Volumes/{CATALOG}/{SOURCE_VOLUME_SCHEMA}/{SOURCE_VOLUME_NAME}'

CROP_FILE_NAME = 'crop_trend.csv'
WEATHER_FILE_NAME = 'province_weather_quarterly.csv'
CROP_FILE_PATH = f'{SOURCE_VOLUME_PATH}/{CROP_FILE_NAME}'
WEATHER_FILE_PATH = f'{SOURCE_VOLUME_PATH}/{WEATHER_FILE_NAME}'

# ----