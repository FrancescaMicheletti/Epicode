# Quanti ordini sono stati consegnati con corriere? Qual è il metodo di pagamento scelto per questi ordini?
SELECT spedizione.nome tipo_spedizione, pagamento.nome metodo_pagamento, count(spedizione.nome) numero_ordini
FROM ordine 
JOIN pasp01 on ordine.paspid = pasp01.paspid 
JOIN spedizione on pasp01.spid = spedizione.spid 
JOIN pagamento on pagamento.paid = pasp01.paid
WHERE pasp01.spid = 2
GROUP BY spedizione.nome, pagamento.nome
;

# Quanti ordini sono stati consegnati in posta? Qual è il metodo di pagamento scelto per questi ordini?
SELECT spedizione.nome tipo_spedizione, pagamento.nome metodo_pagamento, count(spedizione.nome) numero_ordini
FROM ordine 
JOIN pasp01 on ordine.paspid = pasp01.paspid 
JOIN spedizione on pasp01.spid = spedizione.spid 
JOIN pagamento on pagamento.paid = pasp01.paid
WHERE pasp01.spid = 3
GROUP BY spedizione.nome, pagamento.nome
;

## quanti sono gli utenti iscritti alla newsletter?
SELECT count(utente.newsletter) FROM ecommerce.utente
where utente.newsletter = 1;

#quanti utenti hanno partita iva?
SELECT count(utente.piva) FROM ecommerce.utente
where utente.newsletter IS NOT NULL;

# Quanti utenti hanno come provincia Pistoia nel loro indirizzo principale ?
select provincia, conteggio from
(SELECT indirizzo.provincia provincia, count(indirizzo.provincia) conteggio FROM ecommerce.indirizzo
WHERE indirizzo.principale = 1
GROUP BY indirizzo.provincia) as q
where provincia = 'Pistoia' 
;

# Qual è il numero medio di articoli per ordine?
SELECT round(AVG(num_articoli)) FROM (
SELECT oid, sum(quantita) num_articoli FROM ecommerce.orpr01
group by orpr01.oid) AS media_num_art;

# Qual è l'importo medio speso per ordine?
SELECT AVG(spesa_tot) FROM (
SELECT oid, sum(quantita*prezzo) spesa_tot FROM ecommerce.orpr01
group by orpr01.oid) AS spesa_media;

# numero utenti che hanno fatto almeno un ordine
SELECT sum(conteggio)  FROM (
SELECT ordine.uid, count(ordine.uid) conteggio , ordine.oid FROM ecommerce.ordine 
group by ordine.uid
having conteggio >= 1) AS utenti_attivi
;

# numero utenti che hanno fatto più di un ordine
SELECT sum(conteggio)  FROM (
SELECT ordine.uid, count(ordine.uid) conteggio , ordine.oid FROM ecommerce.ordine 
group by ordine.uid
having conteggio > 1) AS utenti_fidelizzati
;

#Quale è la categoria più venduta? Con quanti pezzi?
SELECT cat, max(art_per_cat) FROM
(SELECT prodotto.pid, categoria.cid, categoria.nome cat, sum(orpr01.quantita) art_per_cat FROM ecommerce.orpr01
join prodotto on orpr01.pid = prodotto.pid
join categoria on categoria.cid = prodotto.cid
group by categoria.cid) AS cat_piu_venduta
;

# Numero di prodotti in catalogo per marca in ordine alfabetico
SELECT marca.nome, count(prodotto.pid) num_prodotti FROM ecommerce.marca
join prodotto on prodotto.mid = marca.mid
group by marca.mid
order by marca.nome;
