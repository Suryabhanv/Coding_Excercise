# api/utils.py

from django.db import connection

def search_companies_by_employees_range(min_employees, max_employees):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT * FROM api_company
            WHERE employees BETWEEN %s AND %s
        """, [min_employees, max_employees])
        return cursor.fetchall()

# Define other custom queries as required
