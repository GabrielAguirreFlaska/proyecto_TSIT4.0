create database disqueria;

use disqueria;

create table genero (
    id_genero int not null auto_increment primary key,
    nombre varchar(50)
);

create table discografica(
    id_discografica int not null auto_increment primary key,
    nombre varchar(50)
);

create table formato(
    id_formato int not null auto_increment primary key,
    tipo varchar(50)
);

create table interprete(
    id_interprete int not null auto_increment primary key,
    nombre varchar(50),
    apellido varchar(50),
    nacionalidad varchar(50),
    foto varchar(100)
);

create table album(
    id_album int auto_increment primary key,
    cod_album int not null,
    nombre varchar(100) not null,
    id_interprete int not null,
    id_genero int not null,
    cant_temas int not null,
    id_discografica int not null,
    id_formato int not null,
    fec_lanzamiento date,
    precio real not null,
    cantidad int not null,
    caratula varchar(100),
    foreign key(id_genero) references genero(id_genero),
    foreign key(id_discografica) references discografica(id_discografica),
    foreign key(id_formato) references formato(id_formato)
    ); 

create table tema(
        id_tema int auto_increment primary key,
        titulo varchar(100),
        duracion time,
        autor varchar(100) not null,
        compositor varchar(100) not null,
        id_album int null,
        id_interprete int null,
        foreign key(id_album) references album(id_album) on delete set null,
        foreign key(id_interprete) references interprete(id_interprete) on delete set null
    );


use disqueria;
/* insert into interprete values (null,'Laura','Pausini','Italia',null);
insert into interprete values (null,'Raúl','DiBlasio','Argentina',null);
insert into interprete values (null,'Richard','Clayderman','Francia',null);
insert into interprete values (null,'Enya','Brennan','Irlanda',null);
insert into interprete values (null,'Vangelis','Papathanasiouss','Grecia',null);
insert into interprete values (null,'Jean Michel','Jarre','Francia',null);
insert into interprete values (null,'La Mona','Gimenez','Argentina',null);
insert into interprete values (null,'Chaqueño','Palavecino','Argentina',null);
insert into interprete values (null,'Hermanos','Pimpinela','Argentina',null);
insert into interprete values (null,'Ulises','Bueno','Argentina',null);
insert into interprete values (null,'Leo','Mattioli','Argentina',null);
insert into interprete values (null,'Carlos','Gardel','Argentina',null);
insert into interprete values (null,'Aztor','Piazzolla','Argentina',null);
insert into interprete values (null,'Michael','Jackson','USA',null);
insert into interprete values (null,'Luis Miguel','Gallego Basteri','Mexico',null);
insert into interprete values (null,'José Luis','Perales','España',null);
insert into interprete values (null,'Julio','Iglesias','España',null);
insert into interprete values (null,'Rosana','Arbelo Gopar','España',null); */

INSERT INTO `interprete` (`id_interprete`, `nombre`, `apellido`, `nacionalidad`, `foto`) VALUES
(1, 'Laura', 'Pausini', 'Italia', NULL),
(2, 'Raúl', 'DiBlasio', 'Argentina', NULL),
(3, 'Richard', 'Clayderman', 'Francia', NULL),
(4, 'Enya', 'Brennan', 'Irlanda', NULL),
(5, 'Vangelis', 'Papathanasiouss', 'Grecia', NULL),
(6, 'Jean Michel', 'Jarre', 'Francia', NULL),
(7, 'La Mona', 'Gimenez', 'Argentina', NULL),
(8, 'Chaqueño', 'Palavecino', 'Argentina', NULL),
(9, 'Hermanos', 'Pimpinela', 'Argentina', NULL),
(10, 'Ulises', 'Bueno', 'Argentina', NULL),
(11, 'Leo', 'Mattioli', 'Argentina', NULL),
(12, 'Carlos', 'Gardel', 'Argentina', NULL),
(13, 'Aztor', 'Piazzolla', 'Argentina', NULL),
(14, 'Michael', 'Jackson', 'USA', NULL),
(15, 'Luis Miguel', 'Gallego Basteri', 'Mexico', NULL),
(16, 'José Luis', 'Perales', 'España', NULL),
(17, 'Julio', 'Iglesias', 'España', NULL),
(18, 'Rosana', 'Arbelo Gopar', 'España', NULL),
(19, 'Indio', 'Solari', 'Argentina', 'Foto'),
(20, 'wwwwwww', 'qqqqqqqqqqqqqq', 'eeee', 'r'),
(21, 'rtrrtrtrtr', 'wer', 'yuiyui', 'Foto'),
(22, 'cccccc', 'c', 'c', 'c'),
(23, 'xxxxxxx', 'cxxxx', 'cxx', 'cx'),
(24, 'ttttttt', 'ttttt', 'tttt', 'ttt'),
(25, 'Gustavo3', 'Godoy3', 'Argentina', 'Foto3'),
(26, 'pepe', 'pepe', 'par', 'Foto'),
(28, 'zxzxzx', 'zxzxzx', 'zx', 'Foto'),
(29, 'ererer', 'erer', 'er', 'Foto'),
(30, 'ererer', 'erer', 'er', 'Foto'),
(31, 'qwqw', 'qw', 'qw', 'Foto'),
(32, 'qweqwe aaaaa', 'aaa', 'a', 'Foto'),
(33, '11111111111111', '222222', '3', 'Foto'),
(34, 'Otro nombre', 'otro apellido', 'asd', 'as'),
(35, 'nuevo nuevo', 'nuevo', 'n', 'Foto'),
(36, 'otro nuevo', 'nuevo apellido', 'Nacionalidad', 'Foto'),
(37, '678', '666777888', 'Nacionalidad', 'Foto');



use disqueria;
insert into discografica values (null,'BMG'),(null,'Sony Music'),(null,'WEA'),(null,'Universal'),(null,'Independiente');

insert into genero values (null,'Pop'),(null,'Tango'),(null,'Bolero'),(null,'Folklore'),(null,'Instrumental'),(null,'Electrónica');


insert into formato values (null,'Compact Disc'),(null,'Cassette'),(null,'Long Play'),(null,'Digital');

/* 
insert into album values (null,1234567,'Lêttre à ma Mère',3,5,10,5,3,'1979-01-01',1000,2,null);
insert into album values (null,1234568,'Las Cosas Que Vives',1,1,12,3,1,'1996-01-01',1000,1,null);
insert into album values (null,1234569,'En Tiempo de Amor',2,5,10,1,1,'1993-01-01',1000,1,null);
insert into album values (null,1234570,'El Piano de América',2,5,10,1,1,'1994-01-01',1000,1,null); */

INSERT INTO `album` (`id_album`, `cod_album`, `nombre`, `id_interprete`, `id_genero`, `cant_temas`, `id_discografica`, `id_formato`, `fec_lanzamiento`, `precio`, `cantidad`, `caratula`) VALUES
(1, 1234567, 'Lêttre à ma Mère', 3, 5, 10, 5, 3, '1979-01-01', 1000, 2, NULL),
(2, 1234568, 'Las Cosas Que Vives', 1, 1, 12, 3, 1, '1996-01-01', 1000, 1, NULL),
(3, 1234569, 'En Tiempo de Amor', 2, 5, 10, 1, 1, '1993-01-01', 1000, 1, NULL),
(4, 1234570, 'El Piano de América', 2, 5, 10, 1, 1, '1994-01-01', 1000, 1, NULL),
(8, 123123123, 'xcvbxcvcb', 1, 1, 12, 1, 1, '0000-00-00', 122, 21212, ''),
(9, 567567, 'lalalaala', 13, 2, 12, 3, 3, '1998-02-25', 123, 10, ''),
(10, 2147483647, 'qewrqwrqwr', 3, 3, 2333333, 1, 1, '0000-00-00', 123, 12, ''),
(11, 324234, 'asdfadsfadsf', 1, 1, 23, 1, 1, '0000-00-00', 323, 333333, ''),
(12, 1212, 'nombre test 12', 4, 5, 1, 5, 4, '0000-00-00', 100, 10000000, ''),
(13, 12333, 'NN', 1, 1, 1212112, 1, 1, '0000-00-00', 123, 5467, ''),
(14, 123, 'No se', 25, 1, 14, 5, 1, '2022-11-05', 100, 100, ''),
(15, 124, 'No se 2', 25, 1, 15, 5, 1, '2022-11-05', 100, 100, ''),
(18, 99999, '99', 1, 1, 9, 1, 1, '0000-00-00', 0, 0, ''),
(19, 7, 'nombre nuevo', 1, 1, 7, 1, 1, '0000-00-00', 0, 0, ''),
(21, 3, '3333', 1, 1, 3, 1, 1, '2022-05-11', 3, 3, ''),
(22, 4, '', 1, 1, 3, 1, 1, '0000-00-00', 0, 0, '');



/* insert into tema values (null,'Lêttre à ma Mère','00:40:00:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Mariage D'Amour",'00:03:00:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Souvenirs D'Enfance",'00:03:00:00','Paul De Senneville','Paul De Senneville',1,3);
insert into tema values (null,"Nostalgie",'00:03:00:00','Paul De Senneville','Paul De Senneville',1,3); */

INSERT INTO `tema` (`id_tema`, `titulo`, `duracion`, `autor`, `compositor`, `id_album`, `id_interprete`) VALUES
(1, 'Lêttre à ma Mère', '00:40:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(2, 'Mariage D\'Amour', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(3, 'Souvenirs D\'Enfance', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(4, 'Nostalgie', '00:03:00', 'Paul De Senneville', 'Paul De Senneville', 1, 3),
(9, '', '00:00:00', 'Autor', 'Compositor', 1, 1),
(10, 'nombre tema', '00:00:00', 'Autor ggggg', 'Compositor gggg', 10, 17),
(11, 'sdfgdfgdfsg', '00:00:00', 'Autor ggg 2', 'Compositor ggg 2', 9, 18),
(12, 'qweqweqweqweq', '01:45:00', 'Anonimo', 'Compositor anonimo', 10, 25),
(13, 'otro tema', '01:46:00', 'Anonimo 2', 'Compositor anonimo 2', 13, 25);

