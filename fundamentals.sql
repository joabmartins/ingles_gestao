-- criar tabela
create table us_president (
	president_id        int,
	president_name      text,
	president_party     text
);

-- chave primária e chave estrangeira
create table supplier (
	supplier_id    int       primary key,
	supplier_name  text
);

create table product (
	product_id     int       primary key,
	product_name	text,
	supplier_id    int,
	foreign key (supplier_id) references supplier (supplier_id)
);

-- campos não nulos e valores únicos
create table customer (
	customer_id	int	primary key,
	customer_name	text	not null,
	email_address	text	unique
);

-- alterar tabela
alter table customer add column zip text;
alter table customer rename column zip to zip_code;
alter table customer drop column zip_code;

-- excluir tabela
drop table customer;

-- inserir dados na tabela
insert into us_president (president_id, president_name, president_party)
values (33, 'Harry Truman', 'Democrat')

-- inserção em lote
INSERT INTO us_president (president_id, president_name, president_party) VALUES
(1, 'George Washington', NULL),
(2, 'John Adams', 'Federalist'),
(3, 'Thomas Jefferson', 'Democratic-Republican'),
(4, 'James Madison', 'Democratic-Republican'),
(5, 'James Monroe', 'Democratic-Republican'),
(6, 'John Quincy Adams', 'Democratic-Republican'),
(7, 'Andrew Jackson', 'Democrat'),
(8, 'Martin Van Buren', 'Democrat'),
(9, 'William Harrison', 'Whig'),
(10, 'John Tyler', 'Whig'),
(11, 'James Polk', 'Democrat'),
(12, 'Zachary Taylor', 'Whig'),
(13, 'Millard Fillmore', 'Whig'),
(14, 'Franklin Pierce', 'Democrat'),
(15, 'James Buchanan', 'Democrat'),
(16, 'Abraham Lincoln', 'Republican'),
(17, 'Andrew Johnson', 'Democrat'),
(18, 'Ulysses Grant', 'Republican'),
(19, 'Rutherford Hayes', 'Republican'),
(20, 'James Abram Garfield', 'Republican'),
(21, 'Chester Arthur', 'Republican'),
(22, 'Grover Cleveland', 'Democrat'),
(23, 'Benjamin Harrison', 'Republican'),
(24, 'Grover Cleveland', 'Democrat'),
(25, 'William McKinley', 'Republican'),
(26, 'Theodore Roosevelt', 'Republican'),
(27, 'William Taft', 'Republican'),
(28, 'Woodrow Wilson', 'Democrat'),
(29, 'Warren Harding', 'Republican'),
(30, 'Calvin Coolidge', 'Republican'),
(31, 'Herbert Hoover', 'Republican'),
(32, 'Franklin Roosevelt', 'Democrat'),
(33, 'Harry Truman', 'Democrat'),
(34, 'Dwight Eisenhower', 'Republican'),
(35, 'John Kennedy', 'Democrat'),
(36, 'Lyndon Johnson', 'Democrat'),
(37, 'Richard Nixon', 'Republican'),
(38, 'Gerald Ford', 'Republican'),
(39, 'Jimmy Carter', 'Democrat'),
(40, 'Ronald Reagan', 'Republican'),
(41, 'George Herbert Walker Bush', 'Republican'),
(42, 'Bill Clinton', 'Democrat'),
(43, 'George W. Bush', 'Republican'),
(44, 'Barack Obama', 'Democrat'),
(45, 'Donald Trump', 'Republican'),
(46, 'Joe Biden', 'Democrat');

-- buscar dados da tabela
select    president_id,
          president_name,
          president_party
from      us_president;

-- buscar dados com condição
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican';

-- buscar dados com ordenação
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican'
order by  president_name;

-- buscar dados com ordenação ascendente e descendente
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican'
order by  president_name desc, president_id asc;

-- selecionar apenas dados nulos
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party is null;

-- selecionar apenas dados não nulos
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party is not null;

-- função para retornar os valores com letras maiúsculas
select    upper(president_name)
from      us_president
where     president_id = 10;

-- função para retornar um valor alternativos no lugar de valores nulos
select	president_name,
		coalesce(president_party, 'No Political Party')
from	     us_president 
where     president_id < 5;

-- função agregadora para contar registros
select	count(*)
from	     us_president
where 	president_party = 'Republican';

-- função para buscar valores agrupados
select	president_party, 
		count(*)
from	     us_president
group by  president_party;
