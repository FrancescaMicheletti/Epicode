-- Query 1 ok
select NomeCantante
from canzone join ESECUZIONE on canzone.CodiceReg=ESECUZIONE.CodiceReg
join AUTORE on ESECUZIONE.TitoloCanzone=AUTORE.TitoloCanzone
where Nome=NomeCantante and Nome like ‘d%’

-- Query 2 ok
select TitoloAlbum
from DISCO join CONTIENE on DISCO.NroSerie=CONTIENE.NroSerieDisco
join ESECUZIONE on CONTIENE.CodiceReg=ESECUZIONE.CodiceReg
where ESECUZIONE.anno is NULL

-- Query 3 ok
select distinct NomeCantante from canzone
where NomeCantante not in
      ( select S1.NomeCantante
        from canzone as S1
        where CodiceReg not in
           ( select CodiceReg
             from canzone S2
             where S2.NomeCantante <> S1.NomeCantante ) )

-- Query 4 ok
select NomeCantante
from canzone
where NomeCantante not in (select S1.NomeCantante
       from canzone as S1 join ESECUZIONE on esecuzione.CodiceReg=S1.CodiceReg
            join canzone as S2 on esecuzione.CodiceReg=S2.CodiceReg
       where S1.NomeCantante<> S2.NomeCantante)

