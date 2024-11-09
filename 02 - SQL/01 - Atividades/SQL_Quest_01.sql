WITH FilmeAluguel_Rankeado AS (
	SELECT 
		C.name AS Categoria,
		F.title as Titulo,
    	count(DISTINCT R.rental_id) as Frequencia,
          ROW_NUMBER() OVER (
            PARTITION BY C.name
				ORDER by count(DISTINCT R.rental_id) DESC, F.title ASC) AS Ranking 
	FROM sakila.rental R
	inner join sakila.inventory I on I.inventory_id = R.inventory_id
	inner join sakila.film F on F.film_id = I.film_id
	inner join sakila.film_category FC on F.film_id = FC.film_id
	inner join sakila.category C on C.category_id = FC.category_id
	where r.rental_date >= '2005-06-15'
	group by C.name, F.title  
)

SELECT 
    Categoria,
    Titulo,
    Frequencia
FROM FilmeAluguel_Rankeado
WHERE Ranking = 2;
