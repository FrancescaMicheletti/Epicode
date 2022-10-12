--DISCO(NroSerie, NroSerie, Anno, Prezzo)
--CONTIENE(NroSerieDisco, CodiceReg, NroProg)
--ESECUZIONE(CodiceReg, TitoloCanz, Anno)
--AUTORE(Nome, TitoloCanzone)
--CANTANTE(NomeCantante, CodiceReg)

--1 I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D'
SELECT DISTINCT AUTORE.Nome
FROM AUTORE
  JOIN ESECUZIONE ON ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone
  JOIN CANTANTE ON ESECUZIONE.CodiceReg = CANTANTE.CodiceReg
WHERE CANTANTE.NomeCantante = AUTORE.Nome AND AUTORE.Nome LIKE "D%";

SELECT DISTINCT AUTORE.Nome
FROM AUTORE, ESECUZIONE, CANTANTE
WHERE (ESECUZIONE.TitoloCanz = AUTORE.TitoloCanzone AND ESECUZIONE.CodiceReg = CANTANTE.CodiceReg) AND
      CANTANTE.NomeCantante = AUTORE.Nome AND AUTORE.Nome LIKE "D%";

--2 I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione
SELECT DISCO.TitoloAlbum
FROM DISCO
  JOIN CONTIENE ON DISCO.NroSerie = CONTIENE.NroSerieDisco
  JOIN ESECUZIONE ON ESECUZIONE.CodiceReg = CONTIENE.CodiceReg
WHERE ESECUZIONE.Anno IS NULL;

SELECT DISCO.TitoloAlbum
FROM DISCO, CONTIENE, ESECUZIONE
WHERE (DISCO.NroSerie = CONTIENE.NroSerieDisco AND ESECUZIONE.CodiceReg = CONTIENE.CodiceReg)
      AND ESECUZIONE.Anno = NULL;

--3 I cantanti che non hanno mai registrato canzoni come solisti
--CodiceReg si ripete più di una volta nella tabella CANTANTE
SELECT CANTANTE.NomeCantante
FROM CANTANTE
WHERE CANTANTE.NomeCantante = ANY(SELECT CANTANTE.NomeCantante
                                  FROM CANTANTE
                                  GROUP BY CANTANTE.CodiceReg
                                  HAVING COUNT(CANTANTE.CodiceReg)>1;


--4 I cantanti che hanno sempre registrato canzoni come solisti
-- CodiceReg si ripete solo 1 volta nella tabella CANTANTE
SELECT CANTANTE.NomeCantante
FROM CANTANTE
GROUP BY CANTANTE.CodiceReg
HAVING COUNT(CANTANTE.CodiceReg)=1;

-- soluzione di FILIPPO
SELECT NomeCantante
FROM CANTANTE
WHERE NomeCantante NOT IN
                     (SELECT C1.NomeCantante
                      FROM CANTANTE AS C1 JOIN ESECUZIONE ON
                      ESECUZIONE.CodiceReg = C1.CodiceReg
                      JOIN CANTANTE AS C2 ON
                           ESECUZIONE.CodiceReg = C2.CodiceReg)
                           
                      WHERE C1.NomeCantante <> C2.NomeCantante);
