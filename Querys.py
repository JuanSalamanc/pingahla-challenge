from fastapi import APIRouter
from sqlalchemy import text
from ConexionDB import moto_conexion

router = APIRouter()

@router.get("/metrics/contrataciones_por_trimestre_2021")
def contrataciones_por_trimestre_2021():
    query = """
        SELECT 
        d.department,
        j.job,
        SUM(CASE WHEN DATE_PART(QUARTER, h.datetime) = 1 THEN 1 ELSE 0 END) AS Q1,
        SUM(CASE WHEN DATE_PART(QUARTER, h.datetime) = 2 THEN 1 ELSE 0 END) AS Q2,
        SUM(CASE WHEN DATE_PART(QUARTER, h.datetime) = 3 THEN 1 ELSE 0 END) AS Q3,
        SUM(CASE WHEN DATE_PART(QUARTER, h.datetime) = 4 THEN 1 ELSE 0 END) AS Q4
        FROM hired_employees h
        JOIN departments d ON h.department_id = d.id
        JOIN jobs j ON h.job_id = j.id
        WHERE DATE_PART(YEAR, h.datetime) = 2021
        GROUP BY d.department, j.job
        ORDER BY d.department, j.job;
    """
    with moto_conexion.connect() as conn:
        result = conn.execute(text(query))
        return [dict(row._mapping) for row in result]

@router.get("/metrics/departamentos_sobre_promedio")
def departamentos_sobre_promedio():
    query = """
        WITH hires_per_dept AS (
            SELECT 
                d.id,
                d.department,
                COUNT(*) AS hired
            FROM hired_employees h
            JOIN departments d ON h.department_id = d.id
            WHERE EXTRACT(YEAR FROM h.datetime) = 2021
            GROUP BY d.id, d.department
        ),
        avg_hires AS (
            SELECT AVG(hired) AS avg_hired FROM hires_per_dept
        )
        SELECT 
            h.id,
            h.department,
            h.hired
        FROM hires_per_dept h
        JOIN avg_hires a ON h.hired > a.avg_hired
        ORDER BY h.hired DESC;
    """
    with moto_conexion.connect() as conn:
        result = conn.execute(text(query))
        return [dict(row._mapping) for row in result]

