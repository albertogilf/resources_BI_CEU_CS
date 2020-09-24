DELETE FROM population WHERE reference = 1;

/*EJERCICIO3*/
/*1. Abrir un archivo que contenga una población de ratones (por defecto o pidiendo
el nombre al usuario). La estructura del fichero se indica mediante un fichero de
ejemplo.*/

    /*no se hace ninguna sentencia sql*/


/*2.Crear una población virtual de ratones a partir del tamaño de la población, 
el porcentaje de machos, hembras y mutaciones. */

INSERT INTO population(name,researcher,start_date,num_days) VALUES("population2","researcher2","2020-03-22",250);

INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (41, 'rodolfo', '2020-03-22', 70.134, 'MALE', 37.00, '', 'X', 'Y', 2,NULL,NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (42, 'lilo', '2020-03-22', 88.492, 'FEMALE', 36.82, '', 'X', 'X', 2,NULL,NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (43, 'pompon', '2020-03-22',92.128, 'MALE', 36.3, '', 'X', 'Y_MUTATED', 2,NULL,NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (44, 'gin', '2020-03-22', 57.452, 'FEMALE', 36.98, '', 'X', 'X', 2,NULL,NULL);


/*3. Crear una nueva poblacion de ratones*/
INSERT INTO population(name,researcher,start_date,num_days) VALUES("population3","researcher3","2020-02-20",250);


/*4. Listar los códigos de referencia de todos los ratones de una población.*/

SELECT reference FROM mouse 
WHERE id_population = 2;

/*5. Añadir un nuevo ratón a una población ya existente, indicando todos sus datos.*/
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (45, 'bigotes', '2020-03-23', 86.654, 'MALE', 37.12, '', 'X_MUTATED', 'Y', 2,NULL,NULL);


/*6. Añadir un nuevo ratón a una población ya existente indicando su nombre y
asignando mediante funciones aleatorias el sexo, el peso entre 50 y 100 gramos, 
la temperatura entre 36 y 38 grados, y las mutaciones en sus cromosomas con un
porcentaje del % de posibilidades de contener mutaciones en cualquier de sus
cromosomas definidas por un parámetro de la función con valor por defecto de
20%.*/

INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (46, 'tippi', '2020-03-23', 56.929, 'FEMALE', 36.44, '', 'X', 'X', 2,NULL,NULL);


/*7. Eliminar un ratón de una población indicando su código de referencia. Al
seleccionar esta opción se listan todos los ratones por pantalla.*/

DELETE FROM mouse
WHERE reference = 46;

SELECT reference FROM mouse;

/*8. Modificar los datos de un ratón, indicando su código de referencia. */

UPDATE mouse
SET name = "ali", birthdate="2020-03-23", weight=60.2, description="curioso", id_population=3
WHERE reference = 44;

/*9. Ver información detallada de un ratón, habiendo especificado previamente su
código de referencia. */

SELECT * FROM mouse
WHERE reference = 44;


/*10. Insertar familias con las condiciones de el pdf, las tablas ya estan creadas*/
/*a*/
    /*macho normal hembra normal*/
INSERT INTO family(id,id_father,id_population) VALUES (1,1,1);
INSERT INTO normal_family(id,id_normal_mother) VALUES (1,17);

    /*macho esteril hembra normal*/
INSERT INTO family(id,id_father,id_population) VALUES (2,14,1);
INSERT INTO normal_family(id,id_normal_mother) VALUES (2,18);

    /*macho normal hembra esteril*/
INSERT INTO family(id,id_father,id_population) VALUES (3,2,1);
INSERT INTO normal_family(id,id_normal_mother) VALUES (3,37);

/*b*/
    /*macho poligamico con hembra*/
INSERT INTO family(id,id_father,id_population) VALUES (4,15,1);
INSERT INTO polygamous_family(id) VALUES (4);

UPDATE mouse
SET id_polygamous_mother=4
WHERE reference = 22;

UPDATE mouse
SET id_polygamous_mother=4
WHERE reference = 23;

UPDATE mouse
SET id_polygamous_mother=4
WHERE reference = 38;

/*.Una vez formadas las familias de ratones, comienza la simulacion de reproduccion
de familias, crear hijos*/

/*a cria/crias de macho normal y hembra normal*/
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (47, 'martita', '2020-04-1', 55.14, 'FEMALE', 37.01, '', 'X', 'X', 1, 1, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (48, 'pepito', '2020-04-1', 62.22, 'MALE', 36.54, '', 'X_MUTATED', 'Y', 1, 1, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (49, 'palomita', '2020-04-1', 66.44, 'FEMALE', 36.88, '', 'X_MUTATED', 'X_MUTATED', 1, 1, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (50, 'juanito', '2020-04-1', 71.14, 'MALE', 37.53, '', 'X', 'Y', 1, 1, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (51, 'ratoncito', '2020-04-1', 63.73, 'MALE', 37.28, '', 'X', 'Y', 1, 1, NULL);


/*b cria/crias de macho poligamico no esteril y hembras */
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (52, 'paulita', '2020-04-1', 55.14, 'FEMALE', 37.01, '', 'X', 'X', 1, 4, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (53, 'benito', '2020-04-1', 62.22, 'MALE', 36.54, '', 'X', 'Y', 1, 4, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (54, 'anita', '2020-04-1', 70.23, 'FEMALE', 36.29, '', 'X', 'X', 1, 4, NULL);

/*c*/
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (55, 'marina', '2020-04-1', 65.09, 'FEMALE', 37.67, '', 'X', 'X', 1, 2, NULL);
INSERT INTO mouse(reference,name,birthdate,weight,gender,temperature,description,chromosome1,chromosome2,id_population,id_son,id_polygamous_mother) VALUES (56, 'pepito', '2020-04-1', 73.48, 'MALE', 37.33, '', 'X', 'Y', 1, 2, NULL);

/*d si la hembra es esteril*/
    /*no tiene*/

/*12. Guardar*/
    /*no se puede hacer en sql*/
/*13. Guardar como */
    /*no se puede hacer en sql*/



/*EJERCICIO4 DE INDICES*/

ALTER TABLE mouse ADD INDEX(name);