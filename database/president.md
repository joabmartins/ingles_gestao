
## Create Table
- O nome da tabela e colunas devem ter no max 63 char
- use underline para separar palavras: snake case
- por padrão utilizamos nome no singular
- definimos o tipo do dado para cada atributo (text, integer, numeric, date, timestamp, boolean, character)

```
-- comentário
/*
comentário 2
*/
create table us_president (
	president_id        int,
	president_name      text,
	president_party     text
);
```

## Primary/Foreign Key
- chave primária é o campo de identificação única
- a chave primária da tabela vai existir como chave estrangeira na tabela que ela se relaciona
- por conversão a chave estrangeira tem o mesmo nome da chave primária
- referential integrity: ao tentar adicionar um produto ele vai pedir um id de supplier, se não existir na tabela supplier vai dar erro.
```
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
```

## Not Null/Unique
- caso o dev tente adicionar um registro customer sem nome vai dar erro pois o campo é obrigatório
- o banco de dados não permite que um customer tenha o mesmo endereço de email, pois vai ser usado como login
```
create table customer (
	customer_id	int	primary key,
	customer_name	text	not null,
	email_address	text	unique
);
```

## Drop
- exclui algo, entre o drop e o nome do que vai ser excluido coloque o tipo de estrutura.
```
drop table product;
```

## Alter
- altera algo, precisa especificar o que, de que, a origem e como vai ficar
```
alter table customer add column zip text;
alter table customer rename column zip to zip_code;
alter table customer drop column zip_code;
```

## Insert 
- text fields precisam ser envolvidos com single quote
- a quantidade de fields devem ser a mesma de values, e vice-versa, ou será disparado exception: The Number of Columns Must Match the Number of Values
- recomenda-se sempre declarar os fields, pois senão, no futuro, quando alterar a tabela vai dar erro em cascata.
```
insert into us_president (president_id, president_name, president_party)
values (33, 'Harry Truman', 'Democrat')

select * from us_president;
```

- populando a tabela
```
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
```

- é possível inserir dados de uma tabela para outra.
```
create table us_republican_president (
	president_id	int		primary key,
	president_name	text
);

insert into us_republican_president (
	president_id,
	president_name
)
select	president_id,
		president_name
from	us_president 
where	president_party = 'Republican';

select * from us_republican_president;
```

# Select

```
select    president_id,
          president_name,
          president_party
from      us_president;
```

- where: buscar por um valor de coluna específico
```
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican';
```
- order by: ordenar por uma coluna específica
```
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican'
order by  president_name;
```

- desc/asc: ordena por ordem descendente (default) ou ascendente (inversa)
- é possível colocar uma segunda ordenação se a primeira falhar (mesmo nome)
```
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party = 'Republican'
order by  president_name desc, president_id asc;
```

- null: George Washington não tinha partido político, então a coluna party é vazia/nula.
Ele se opunha à ideia de facções e partidos, acreditando que eles dividiam a nação e promoviam interesses particulares em vez do bem comum. Essa preocupação foi um tema central em seu Discurso de Despedida.
```
select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party is null;

select    president_id,
          president_name,
          president_party
from      us_president 
where     president_party is not null;
```

## Funções
### upper
- coloca em maiúsculo
```
select    upper(president_name)
from      us_president
where     president_id = 10;
```
### coalesce
- imprime uma mensagem ao invés de null
```
select	president_name,
		coalesce(president_party, 'No Political Party')
from	     us_president 
where     president_id < 5;
```
### aggregate functions
- recebe múltiplos valores mas retorna apenas um
count: conta a quantidade de registros
max/min: retorna o valor máximo/mínimo
avg: retorna a média, o valor médio
sum: retorna a soma dos valores do select
```
select	count(*)
from	     us_president
where 	president_party = 'Republican';
```
### group by
- agrupa os valores
```
select	president_party, 
		count(*)
from	     us_president
group by  president_party;
```

## challenge
```
CREATE TABLE countries (
	id 			SERIAL 		PRIMARY KEY,
	country_name 	VARCHAR(255) 	NOT NULL,
	population 	BIGINT,
	area 		INT,
	continent 	VARCHAR(255)
);


INSERT INTO countries (country_name, population, area, continent) VALUES
-- América do Norte
('Estados Unidos', 331900000, 9834000, 'América do Norte'),
('Canadá', 38700000, 9985000, 'América do Norte'),
('México', 126700000, 1964000, 'América do Norte'),
('Cuba', 11200000, 109884, 'América do Norte'),
('Honduras', 10200000, 112492, 'América do Norte'),
-- América do Sul
('Brasil', 215300000, 8515767, 'América do Sul'),
('Argentina', 45800000, 2780400, 'América do Sul'),
('Colômbia', 51500000, 1141748, 'América do Sul'),
('Chile', 19600000, 756102, 'América do Sul'),
('Peru', 33700000, 1285216, 'América do Sul'),
-- Europa
('Alemanha', 83200000, 357022, 'Europa'),
('França', 65500000, 643801, 'Europa'),
('Reino Unido', 67300000, 242495, 'Europa'),
('Itália', 58900000, 301340, 'Europa'),
('Espanha', 47500000, 505990, 'Europa'),
-- África
('Nigéria', 218500000, 923768, 'África'),
('Egito', 109300000, 1010408, 'África'),
('Etiópia', 123400000, 1104300, 'África'),
('África do Sul', 60400000, 1221037, 'África'),
('Quênia', 54000000, 580367, 'África'),
-- Ásia
('China', 1425000000, 9596961, 'Ásia'),
('Índia', 1417000000, 3287590, 'Ásia'),
('Indonésia', 275500000, 1904569, 'Ásia'),
('Japão', 125100000, 377975, 'Ásia'),
('Rússia', 144700000, 17125200, 'Ásia'),
-- Oceania
('Austrália', 26000000, 7692024, 'Oceania'),
('Nova Zelândia', 5100000, 268021, 'Oceania');

select 		continent,
			sum(population) ,
			sum(area)
from 		countries
group by	continent;

-- alias
select 		continent,
			sum(population)     as population_total,
			sum(area)	          as area_total
from 		countries
group by	continent;
```