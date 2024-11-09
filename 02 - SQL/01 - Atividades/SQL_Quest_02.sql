SELECT 
	C.name AS Categoria, 
    count(DISTINCT R.rental_id) as Frequencia
FROM rental R
inner join inventory I on I.inventory_id = R.inventory_id
inner join film F on F.film_id = I.film_id
inner join film_category FC on F.film_id = FC.film_id
inner join category C on C.category_id = FC.category_id
where r.rental_date >= '2005-06-15'
group by C.name
HAVING Frequencia >= 1000 
ORDER BY Frequencia DESC