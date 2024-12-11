-- MySQL
SELECT 
    cols.COLUMN_NAME,
    cols.COLUMN_TYPE,
    cols.CHARACTER_MAXIMUM_LENGTH AS column_length,
    cols.NUMERIC_PRECISION AS numeric_precision,
    cols.NUMERIC_SCALE AS numeric_scale,
    cols.IS_NULLABLE,
    cols.COLUMN_KEY,
    refs.REFERENCED_TABLE_NAME AS foreign_table,
    refs.REFERENCED_COLUMN_NAME AS foreign_column
FROM 
    INFORMATION_SCHEMA.COLUMNS cols
LEFT JOIN 
    INFORMATION_SCHEMA.KEY_COLUMN_USAGE refs
    ON cols.TABLE_NAME = refs.TABLE_NAME 
    AND cols.COLUMN_NAME = refs.COLUMN_NAME
    AND refs.REFERENCED_TABLE_NAME IS NOT NULL
WHERE 
    cols.TABLE_SCHEMA = 'nome_do_esquema'
    AND cols.TABLE_NAME = 'nome_da_tabela';