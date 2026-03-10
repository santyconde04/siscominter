CREATE TABLE capitulos(

capitulo CHAR(2) PRIMARY KEY,
descripcion TEXT

);

CREATE TABLE nomenclador(

id SERIAL PRIMARY KEY,
codigo VARCHAR(20),
capitulo CHAR(2),
partida CHAR(4),
subpartida CHAR(6),
item CHAR(3),
sufijo CHAR(2),
descripcion TEXT

);

CREATE TABLE sufijos(

id SERIAL PRIMARY KEY,
posicion VARCHAR(10),
sufijo VARCHAR(10),
descripcion TEXT

);