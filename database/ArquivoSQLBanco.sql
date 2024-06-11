CREATE DATABASE Banco;
USE Banco;

-------------------------------------------------------------------------------------------

CREATE TABLE TBUsuario(
	IDUsuario int not null,
	Nome varchar(150) not null,
	CPF varchar(14) not null,
	UsuarioPresente bit not null,
	PRIMARY KEY(IDUsuario)
);
SELECT * FROM TBUsuario;

-----------------------------------

CREATE TABLE TBCarro(
	IDCarro int identity(1,1) not null,
	Placa varchar(7) not null,
	COD_Dono int,
	PRIMARY KEY(IDCarro),
	FOREIGN KEY(Cod_Dono) REFERENCES TBUsuario(IDUsuario)
);

SELECT * FROM TBCarro;

-----------------------------------

CREATE TABLE TBPresente(
	IDPresente int not null,
	FOREIGN KEY(IDPresente) REFERENCES TBCarro(IDCarro)
);

SELECT * FROM TBPresente;


-------------------------------------------------------------
--CRUD - CREATE

INSERT INTO TBUsuario VALUES
(10, 'Evandro', '123.456.789/10', 0);

INSERT INTO TBUsuario VALUES
(20, 'Sérgio', '223.456.789/10', 0);

--CRUD - READ

SELECT * FROM TBUsuario;

--CRUD - UPDATE

UPDATE TBUsuario 
SET UsuarioPresente = 1
WHERE IDUsuario = 10;

--CRUD - DELETE

DELETE FROM TBUsuario
WHERE IDUsuario = 10;

