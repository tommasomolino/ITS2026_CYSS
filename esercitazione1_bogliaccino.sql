use cyss2026;

SHOW TABLES;

DESCRIBE libri;

CREATE TABLE libri (
    libro_id int PRIMARY key AUTO_INCREMENT, # NOT NULL & UNIQUE
    titolo VARCHAR(50) NOT NULL,
    pagine int NOT NULL DEFAULT 0,
    prezzo DECIMAL(5,2) NOT NULL DEFAULT 0.0
);

alter table libri
add column editore_id int; 

# CRUD su libri

## CREATE
INSERT INTO libri (titolo, pagine, prezzo, editore_id) VALUES ('Tu robot', 123, 10.50, 3);

## READ - RETRIEVE
SELECT titolo, prezzo FROM libri;
SELECT * FROM libri;

## UPDATE
UPDATE libri set prezzo = 20.65 WHERE libro_id = 3;
UPDATE libri set editore_id = 1 WHERE libro_id <= 3;
UPDATE libri set editore_id = 2 WHERE libro_id=4;
## DELETE
DELETE FROM libri WHERE libro_id = 2;


create table editori (
    editore_id int PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(30) not null,
    email VARCHAR(100),
    persona_contatto VARCHAR(100)
);

INSERT INTO editori VALUES (0, 'Feltrinelli', 'feltrinelli@feltrinelli.it', 'Sig.ra Giovanna 345.67891011');

SELECT * FROM editori;
SELECT * FROM libri;

SELECT 
    libri.titolo, 
    libri.prezzo,
    editori.nome as editore
FROM libri, editori
WHERE libri.editore_id = editori.editore_id;

ALTER TABLE libri
ADD CONSTRAINT fk_libri_editori FOREIGN KEY (editore_id) 
REFERENCES editori(editore_id)
ON DELETE CASCADE
ON UPDATE CASCADE;

