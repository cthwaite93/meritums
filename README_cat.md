# Meritums

Aquest petit programa assigna candidats a les seves respectives especialitats. Les especialitats tenen un aforament limitat i els candidats estan ordenats per descendència tenint en compte els **punts** que tenen.

## Dades

Les dades estan extretes d'un fitxer .json creat pel següent lloc web: https://www.sindicat.net/llistat-provisional-concurs-de-merits-2022-2023/. Podeu fer una sol·licitud GET i obtenir tots els candidats en un sol fitxer.
Com podreu veure, això vol dir que tenim **62.937 registres**, aquest nombre de registres coincideix amb les [llistes de la Generalitat oficials](https://educacio.gencat.cat/web/.content/home/arees-actuacio/professors/oposicions/ingres-acces-cossos-docents/concurs-merits/valoracio-provisional/llista-provisional-merits-cos-especialitat.pdf).

### Exempció de responsabilitat

El resultat de l'algoritme va en funció de les dades que han sigut tractades i provenen de fonts no oficials. Les dades oficials les teniu al link anterior.

### Tractament de les dades

Com que les dades d'aquesta llista no tenen el DNI parcial, vaig haver d'esbrinar una manera d'identificar un candidat. 
Com podeu veure, els candidats poden fer les sol·licituds que vulguin en llistes diferents, i han decidit una prioritat per cada llista. 
Així que primer vaig analitzar les dades per trobar si hi havia més de dos candidats amb el mateix **nom complet** i prioritat **1**. 
A causa de la meva sort, i de gent que tenia cognoms semblants, hi havien molts conflictes. Això significava que no podia discernir: qui era qui **(DOLOR)!**
\
\
Així que mirant els conflictes, em vaig adonar que semblava que candidats amb el mateix nom complet estaven en diferents tribunals *(uff)*. 
Vaig decidir implementar una identificació personalitzada concatenant el nom complet i el tribunal:

https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/candidate.py#L13

Bé, això em va deixar un conflicte... així que vaig editar les dades i alguna Judit és *Judit2*.

## Algorisme

Per tant, a la part realment interessant: **Com assigno els candidats a la seva especialitat respectiva?**
\
\
Ara, hom diria: *Bé, tenim en compte només la primera prioritat de tots els candidats, ordenem-los per punts i afegim-los a la seva especialitat.*
\
\
**PERÒ**, i és un gran però, això no seria just. I si algú tingués més punts que un altre però amb una prioritat més baixa?
\
Personalment crec que qualsevol persona té dret a provar i accedir a qualsevol especialitat si pot, i l'única cosa a tenir en compte són els seus **mèrits** 
, no la seva prioritat.
\
\
Així que el que faig és el següent:
* Poso tots els candidats en una llista.
* Els ordeno per prioritat ascendent i si són iguals, per punts descendents.
https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/candidate.py#L15-L20
* L'algorisme no s'aturarà fins que la llista de candidats estigui buida, això vol dir que tots els candidats han tingut l'oportunitat de ser membres d'una especialitat tenint en compte les seves prioritats.
* Agafem un candidat i l'assignem a l'especialitat que ha escollit, tret que el candidat ja hagi estat assignat a una especialitat.
    - Si el candidat no està assignat perquè ja ho ha està en un altra especialitat, aquest intent passa a una llista d'espera per si és expulsat d'aquella llista més endevant.
* Si hi ha espai a la llista de l'especialitat, cap dins.
    - En cas contrari, veurem si l'últim membre de la llista té menys punts que el candidat i substituïm aquest membre
    - **SI TENEN ELS MATEIXOS PUNTS, PRIORITZO LA SEVA PRIORITAT I SI ÉS LA MATEIXA DEIXO EL QUE HI HA HI ERA A LA LLISTA, NO TINC PROU DADES PER APLICAR DESEMPATS.**
    https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/specialty.py#L15-L29
* Si afegint un nou candidat hem expulsat algú, comprovem si alguns dels intents del candidat estan a la llista d'espera, els tornem a afegir a la llista de candidats perquè tinguin l'oportunitat de ser assignats a una especialitat.
\
\
Tot s'executa en ments de 2 segons, n'estic molt content.

## Resultats
Teniu totes les llistes d'especialitats generades en una carpeta. Són fitxers .csv.
