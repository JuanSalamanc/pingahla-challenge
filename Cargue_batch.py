import pandas as pd
from io import BytesIO
from sqlalchemy import text
from ConexionDB import moto_conexion

def carga_csv_batch(table_name, file_bytes):
    df = pd.read_csv(BytesIO(file_bytes),  header=None)

    if table_name == "departments":
        df.columns = ["id", "department"]
    elif table_name == "jobs":
        df.columns = ["id", "job"]
    elif table_name == "hired_employees":
        df.columns = ["id", "name", "datetime", "department_id", "job_id"]
        df["datetime"] = pd.to_datetime(df["datetime"], errors="coerce")
    else:
        return f"Tabla no reconocida: {table_name}"

    with moto_conexion.connect() as conn:
        result = conn.execute(text(f"SELECT MAX(ID) FROM {table_name}"))
        last_id = result.scalar()
        if last_id is None:
            last_id = 0

    df_filtered = df[df["id"] > last_id]

    df_filtered = df_filtered.head(1000)

    if df_filtered.empty:
        return f"No hay registros nuevos por encima del ID {last_id}. No se insertó nada."

    df_filtered.to_sql(table_name, moto_conexion, if_exists="append", index=False)
    return f"{len(df_filtered)} registros insertados en {table_name} desde ID > {last_id}"