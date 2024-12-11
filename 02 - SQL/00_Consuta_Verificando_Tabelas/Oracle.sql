

-- Oracle
SELECT 
    cols.column_name,
    cols.data_type,
    cols.data_length AS column_length,
    cols.data_precision AS numeric_precision,
    cols.data_scale AS numeric_scale,
    cols.nullable,
    cons.constraint_type,
    fk.referenced_table,
    fk.referenced_column
FROM 
    all_tab_columns cols
LEFT JOIN 
    (
        SELECT 
            a.table_name AS fk_table,
            a.column_name AS fk_column,
            c_pk.table_name AS referenced_table,
            b.column_name AS referenced_column
        FROM 
            all_cons_columns a
        JOIN 
            all_constraints c_fk 
            ON a.constraint_name = c_fk.constraint_name
        JOIN 
            all_cons_columns b 
            ON c_fk.r_constraint_name = b.constraint_name
        JOIN 
            all_constraints c_pk 
            ON b.constraint_name = c_pk.constraint_name
        WHERE 
            c_fk.constraint_type = 'R'
    ) fk
    ON cols.table_name = fk.fk_table AND cols.column_name = fk.fk_column
LEFT JOIN 
    all_constraints cons
    ON fk.fk_table = cons.table_name AND cols.column_name = fk.fk_column
WHERE 
    cols.table_name = 'NOME_DA_TABELA';