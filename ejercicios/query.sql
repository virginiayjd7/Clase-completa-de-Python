create database curso;
use curso;
create table curso.usuario(
id integer(11)not null auto_increment,
nombre varchar(80)not null,
apellido varchar(80)not null,
fecha_nacimiento datetime null,
primary key (id)
);
drop table if exists usuario;
alter table usuario add column telefono varchar(45) NULL;
alter table usuario modify column telefono varchar(30) NULL;/*SI EL NUMERO O DATOS ESTA GRANDE ENCONTE SE CORTARA*/
/* EL FORMATO DE FECHA ES AÑO MS DIA Y HORA*/
insert into usuario(
nombre,apellido,fecha_nacimiento,telefono)
values ('Virginia', 'Aquino','1994-12-10 10:00:00','975957226');

select * from usuario;
select id,nombre,apellido from usuario;
delete from usuario where id='1';
select * from usuario where id='1';
update usuario
set nombre='janeth',
apellido='huallpa'
where id ='2';

SELECT * FROM usuario where apellido = 'janeth'
and nombre = 'ssddd';
SELECT * FROM usuario where apellido = 'janeth'
or nombre = 'ssddd';

SELECT count(*) as 'Cantidad' FROM usuario 
where apellido = 'janeth'
and nombre = 'ssddd';

SELECT nombre as 'Cantidad' FROM usuario 
where apellido = 'janeth'
and nombre = 'ssddd';

SELECT * FROM usuario 
where apellido like '%a%';/*para buscar*/

create table publicaciones(
id int(11) not null auto_increment,
autor_id int (11) not null,
titulo varchar(150) not null,
texto text not null,
primary key (id),
foreign key(autor_id) references usuario(id)
);
/*los join son con claves foraneas si en caso no es nesesario si estan unidos f foranea  solo en casos de join */
select p.id,
p.titulo,
p.texto,
u.id,
CONCAT(u.nombre,'',u.apellido)as 'autor'
from publicaciones p,usuario u
where p.autor_id=u.id;

create table productos(
id int(11)not null auto_increment,
nombre varchar(100),
precio double,
primary key (id)
);

select COUNT(*) from productos;/*CUENTA FILAS*/
select MAX(precio) from productos;/*maximo*/
select AVG(precio) from productos;
select SUM(precio) from productos