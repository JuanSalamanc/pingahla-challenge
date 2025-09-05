from sqlalchemy import create_engine, text

USER = "JUANSALAMANCA03"
PASSWORD = "ColombiaBogota2025#"
ACCOUNT = "JAHZUUO-OIC57828"
WAREHOUSE = "COMPUTE_WH"
DATABASE = "SNOWFLAKE_LEARNING_DB"
SCHEMA = "JUANSALAMANCA03_LOAD_SAMPLE_DATA_FROM_S3"

cadena_conexion = (
    f"snowflake://{USER}:{PASSWORD}@{ACCOUNT}/{DATABASE}/{SCHEMA}?warehouse={WAREHOUSE}"
)

moto_conexion = create_engine(cadena_conexion)

try:
    with moto_conexion.connect() as conn:
        result = conn.execute(text("SELECT CURRENT_VERSION()"))
        for row in result:
            print("Conexión exitosa. Snowflake:", row[0])
except Exception as e:
    print("Error al conectar:", e)