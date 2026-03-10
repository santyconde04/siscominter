TRUNCATE capitulos;
TRUNCATE nomenclador;
TRUNCATE sufijos;

\copy capitulos FROM 'data_processed/capitulos.csv' DELIMITER ',' CSV HEADER

\copy nomenclador(codigo,descripcion) FROM 'data_processed/nomenclador.csv' DELIMITER ',' CSV HEADER

\copy sufijos(posicion,sufijo,descripcion) FROM 'data_processed/sufijos.csv' DELIMITER ',' CSV HEADER