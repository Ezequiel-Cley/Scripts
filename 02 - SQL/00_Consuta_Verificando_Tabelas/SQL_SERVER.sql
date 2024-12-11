





--SQL SERVER

SELECT 
    c.name AS column_name,
    t.name AS data_type,
    c.max_length AS column_length,
    c.precision AS numeric_precision,
    c.scale AS numeric_scale,
    c.is_nullable,
    CASE 
        WHEN fk.parent_object_id IS NOT NULL THEN 'FOREIGN KEY'
        WHEN i.is_primary_key = 1 THEN 'PRIMARY KEY'
        ELSE NULL
    END AS constraint_type,
    ref_table.name AS foreign_table,
    ref_column.name AS foreign_column
FROM 
    sys.columns c
JOIN 
    sys.types t ON c.user_type_id = t.user_type_id
LEFT JOIN 
    sys.foreign_key_columns fk 
    ON c.object_id = fk.parent_object_id AND c.column_id = fk.parent_column_id
LEFT JOIN 
    sys.tables ref_table 
    ON fk.referenced_object_id = ref_table.object_id
LEFT JOIN 
    sys.columns ref_column 
    ON fk.referenced_object_id = ref_column.object_id AND fk.referenced_column_id = ref_column.column_id
LEFT JOIN 
    sys.index_columns ic 
    ON c.object_id = ic.object_id AND c.column_id = ic.column_id
LEFT JOIN 
    sys.indexes i 
    ON ic.index_id = i.index_id AND ic.object_id = i.object_id
WHERE 
    c.object_id = OBJECT_ID('Nome_da_Tabela');

