


drop database conjunto_ratones;
create database conjunto_ratones;
use conjunto_ratones;

CREATE TABLE population(
    reference INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    researcher VARCHAR(30) NOT NULL,
    start_date DATE NOT NULL,
    num_days INT NOT NULL CHECK(num_days<=270)
)ENGINE=INNODB;


CREATE TABLE mouse(
    reference INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    weight INT NOT NULL,
    gender ENUM("MALE","FEMALE") NOT NULL,
    temperature INT NOT NULL,
    description VARCHAR(255) NOT NULL,
    chromosome1 ENUM("X","X_MUTATED") NOT NULL,
    chromosome2 ENUM("X","X_MUTATED","Y","Y_MUTATED") NOT NULL,
    id_population INT,
    CONSTRAINT id_population_constraint_1 FOREIGN KEY (id_population) REFERENCES population(reference) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;


CREATE TABLE family(
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_father INT NOT NULL UNIQUE,
    id_population INT NOT NULL,
    CONSTRAINT id_father_constraint FOREIGN KEY (id_father) REFERENCES mouse(reference) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT id_population_family_costraint FOREIGN KEY (id_population) REFERENCES population(reference) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;

ALTER TABLE mouse ADD id_son INT DEFAULT NULL;
ALTER TABLE mouse ADD CONSTRAINT id_son_constraint FOREIGN KEY (id_son) REFERENCES family(id) ON DELETE CASCADE ON UPDATE CASCADE;

CREATE TABLE normal_family(
    id INT PRIMARY KEY,
    id_normal_mother INT NOT NULL UNIQUE,
    CONSTRAINT id_normal_family FOREIGN KEY (id) REFERENCES family(id) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT id_normal_mother_constraint FOREIGN KEY (id_normal_mother) REFERENCES mouse(reference) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;

CREATE TABLE polygamous_family(
    id INT PRIMARY KEY,
    CONSTRAINT id_family_polygamous FOREIGN KEY (id) REFERENCES family(id) ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE=INNODB;

ALTER TABLE mouse ADD id_polygamous_mother INT DEFAULT NULL;
ALTER TABLE mouse ADD CONSTRAINT id_polygamous_mother_constraint FOREIGN KEY (id_polygamous_mother) REFERENCES polygamous_family(id) ON DELETE CASCADE ON UPDATE CASCADE;

