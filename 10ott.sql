--AEROPORTO (Citta,Nazione,NumPiste)
--VOLO (IdVolo,GiornoSett,CittaPart,OraPart,CittaArr,OraArr,TipoAereo)
--AEREO (TipoAereo,NumPasseggeri,QtaMerci)

--1.	Le città con un aeroporto di cui non è noto il numero di piste
SELECT Citta FROM AEROPORTO WHERE NumPiste IS NULL;
SELECT AEROPORTO.Citta FROM AEROPORTO WHERE AEROPORTO.NumPiste IS NULL;
SELECT A.Citta FROM AEROPORTO AS A WHERE A.NumPiste IS NULL;
SELECT A.Citta AS C FROM AEROPORTO AS A WHERE A.NumPiste IS NULL;

--2.	I tipi di aereo usati nei voli the partono da Torino
SELECT TipoAereo FROM VOLO WHERE CittaPart = “Torino”;
SELECT VOLO.TipoAereo FROM VOLO WHERE VOLO.CittaPart = “Torino”;
SELECT V.TipoAereo FROM VOLO AS V WHERE V.CittaPart = “Torino” OR V.CittaPart = “torino” OR V.CittaPart = “TORINO”;

--3.	Le città da cui partono voli diretti a Bologna
SELECT CittaPart FROM VOLO WHERE CittaArr = “Bologna”;
SELECT VOLO.CittaPart FROM VOLO WHERE VOLO.CittaArr = “Bologna”;
SELECT V.CittaPart FROM VOLO AS V WHERE V.CittaArr = “Bologna”;

--4.	Le citta da cui parte e arriva il volo con codice AZ274
SELECT CittaPart, CittaArr FROM VOLO WHERE IdVolo = “AZ274”;
SELECT VOLO.CittaPart, VOLO.CittaArr FROM VOLO WHERE VOLO.IdVolo = “AZ274”;
SELECT V.CittaPart, V.CittaArr FROM VOLO AS V WHERE V.IdVolo = “AZ274”;

--5.	II tipo di aereo, il giorno della settimana, l’orario di partenza
--la cui citta di partenza inizia per B e contiene O e la cui città di arrivo termina con A e contiene E
SELECT TipoAereo, GiornoSett, OraPart FROM VOLO WHERE CittaPart LIKE “B%O%” AND CittaArr LIKE “%E%A”;
SELECT VOLO.TipoAereo, VOLO.GiornoSett, VOLO.OraPart FROM VOLO WHERE VOLO.CittaPart LIKE “B%O%” AND VOLO.CittaArr LIKE “%E%A”;
SELECT V.TipoAereo, V.GiornoSett, V.OraPart FROM VOLO AS V WHERE V.CittaPart LIKE “B%O%” AND V.CittaArr LIKE “%E%A”;
