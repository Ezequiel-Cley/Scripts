
-- PostgreeSQL

SELECT 
    c.column_name,
    c.data_type,
    c.character_maximum_length AS column_length,
    c.numeric_precision AS numeric_precision,
    c.numeric_scale AS numeric_scale,
    c.is_nullable,
    tc.constraint_type,
    fk.referenced_table,
    fk.referenced_column
FROM 
    information_schema.columns c
LEFT JOIN 
    information_schema.key_column_usage k
    ON c.table_name = k.table_name AND c.column_name = k.column_name
LEFT JOIN 
    information_schema.table_constraints tc
    ON k.constraint_name = tc.constraint_name AND tc.table_name = c.table_name
LEFT JOIN 
    (
        SELECT 
            kcu.column_name AS foreign_key_column,
            ccu.table_name AS referenced_table,
            ccu.column_name AS referenced_column,
            kcu.table_name AS fk_table
        FROM 
            information_schema.key_column_usage kcu
        JOIN 
            information_schema.constraint_column_usage ccu
            ON kcu.constraint_name = ccu.constraint_name
    ) fk
    ON c.table_name = fk.fk_table AND c.column_name = fk.foreign_key_column
WHERE 
    c.table_name = 'nome_da_tabela';