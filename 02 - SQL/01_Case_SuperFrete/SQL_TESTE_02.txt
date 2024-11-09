/* Questão a ser Resolvida 
2 - Para o mesmo database proposto, escreva uma query que mostre quais as categorias
de filmes que possuem 1000 locações ou mais a partir de 2005-06-15. Devem ser
retornados pela query apenas os campos de nome da categoria do filme e frequência
(quantidade) de locações de filmes para a categoria, com resultado da query em ordem
decrescente em relação a frequência de locações.
*/

/* Consulta para extração das categoria com mais de 999 alugueis por categoria. */
SELECT 
	C.name AS Categoria, 
    count(DISTINCT R.rental_id) as Frequencia -- Contando de forma distinta os alugeis realizados
FROM rental R
inner join inventory I on I.inventory_id = R.inventory_id -- Cruzamento para Extração do inventorio de filmes 
inner join film F on F.film_id = I.film_id -- Cruzamento para extração dos dados do Filme
inner join film_category FC on F.film_id = FC.film_id -- Cruzamento para Extração da categorias de cada filme
inner join category C on C.category_id = FC.category_id -- Cruzamento para extração do nome das categorias do filme
where r.rental_date >= '2005-06-15' -- Filtrando tudo que for maior que a data (2005-06-15)
group by C.name  -- Agrupando colunas para realizar contagem distinct
HAVING Frequencia >= 1000 -- Filtrando o campo contado onde tem mais de 1000 locações.
ORDER BY Frequencia DESC -- Ordenando as Colunas para retornar em ordem decrescenteactor
