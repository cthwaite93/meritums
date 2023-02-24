# Meritums

Aquest petit programa assigna candidats a les seves respectives especialitats. Les especialitats tenen un aforament limitat i els candidats estan ordenats per criteri descendent (de més a menys) tenint en compte els **punts** que han obtingut.

### Exempció de responsabilitat

El resultat de l'algoritme és en funció de les dades que té d'entrada. Aquestes dades han sigut tractades i provenen de fonts no oficials. Les dades oficials les teniu a l'enllaç inferior.

## Dades

Les dades han sigut extretes d'un fitxer .json creat pel següent lloc web: https://www.sindicat.net/llistat-provisional-concurs-de-merits-2022-2023/. Podeu fer una sol·licitud GET i obtenir tots els candidats en un sol fitxer.
\
Com podreu veure, això vol dir que tenim **62.937 registres**, aquest nombre de registres coincideix amb les [llistes de la Generalitat oficials](https://educacio.gencat.cat/web/.content/home/arees-actuacio/professors/oposicions/ingres-acces-cossos-docents/concurs-merits/valoracio-provisional/llista-provisional-merits-cos-especialitat.pdf).

### Tractament de les dades

Com que les dades d'aquesta llista no tenen el DNI parcial, vaig haver d'esbrinar una manera d'identificar un candidat. 
A més, els candidats poden fer les sol·licituds que vulguin en llistes diferents, i decideixen una prioritat per cada llista.
\
\
Així que primer vaig analitzar les dades per trobar si hi havia més de dos candidats amb el mateix **nom complet** i prioritat **1**. 
A causa de la meva sort, i de gent que tenia cognoms semblants, hi havien molts conflictes. Això significava que no podia discernir: qui era qui **(DOLOR)!**
\
\
Examinant els conflictes, em vaig adonar que candidats amb el mateix nom complet estaven en diferents tribunals *(uff)*. 
Vaig decidir implementar una identificació personalitzada concatenant el nom complet i el tribunal:

https://github.com/cthwaite93/meritums/blob/5bb96bee51dab7e41685ca6cc4fa693d7d1084dd/classes/candidate.py#L10

Bé, això em va deixar un conflicte... així que vaig editar les dades i alguna Judit és *Judit2*.

### Refinament de les dades
Abans d'explicar com funciona l'algorisme, heu de saber que les dades *"originals"* han sigut refinades per millorar el seu processament. Tots els registres d'un candidat s'han unificat en **un de sol per candidat**.
\
En aquest nou registre, tota la informació de les diferents especialitats per les qual concursa (barem, prioritats) són emmagatzemades.
\
Fent això s'han reduït les dades de 62937 a **37333 registres**.

## Algorisme

Comencem la part realment interessant: **Com assigno els candidats a la seva especialitat respectiva?**
\
\
Ara hom diria: *Bé, tenim en compte només la primera prioritat de tots els candidats, ordenem-los per punts i afegim-los a la seva especialitat.*
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
* Els ordeno per criteri descendent tenint en compte els punts de l'especialitat a la que intenta concursar.
https://github.com/cthwaite93/meritums/blob/5bb96bee51dab7e41685ca6cc4fa693d7d1084dd/classes/candidate.py#L43-L44
    - L'especialitat a la que concorre un candidat es sempre aquella que té la prioritat més alta que no ha participat encara en el concurs.
* L'algorisme no s'aturarà fins que la llista de candidats estigui buida, això vol dir que tots els candidats han tingut l'oportunitat de ser membres d'una especialitat tenint en compte les seves prioritats.
* Agafem un candidat, el treiem de la llista i intentem que concursi a l'especialitat que ha escollit.
* Si encara queden places a l'especialitat, cap dins.
    - En cas contrari, veurem si l'últim membre de la llista té menys punts que el candidat i substituïm aquest membre.
    - **SI TENEN ELS MATEIXOS PUNTS, PRIORITZO LA SEVA PRIORITAT I SI ÉS LA MATEIXA DEIXO EL QUE HI HA HI ERA A LA LLISTA, NO TINC PROU DADES PER APLICAR DESEMPATS.**
    https://github.com/cthwaite93/meritums/blob/bbe6589b115f5018fcba299c185d7eacbabd258f/classes/specialty.py#L15-L29
* Si afegint un nou candidat hem expulsat algú, comprovem si encara li queden especialitats a les quals vol concursar.
* Si és així, el tornem a posar a la llista per concursar.
\
\
Tot s'executa en ments de 2 segons, n'estic molt content.

## Resultats
A la carpeta *lists* tens una carpeta per a cadascuna de les especialitats que estan passant pel procés de mèrits.
\
\
Dins de la carpeta d'especialitats, teniu la llista accepted.csv, on trobareu qui ha estat admès a l'especialitat.
\
A més, trobareu la llista rejected.csv, on trobareu els que han estat rebutjats.
\
\
És important indicar que *CAP CANDIDAT* pot estar en més d'una llista acceptada, i si han estat acceptats no apareixeran en cap de les llistes rebutjades *(té sentit)*.
\
\


D'altra banda, un candidat **pot figurar** en una o més llistes rebutjades sinó ha estat seleccionat a cap.
