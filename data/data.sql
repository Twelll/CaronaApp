---SQLITE
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS pessoas (
    id_pessoa INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS carona (
    id_carona INTEGER PRIMARY KEY,
    origem TEXT NOT NULL,
    destino TEXT NOT NULL,
    data_carona DATETIME NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS pessoa_carona (
    id_rel INTEGER PRIMARY KEY,
    id_carona INTEGER NOT NULL,
    id_pessoa INTEGER NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pago', 'pendente')),
    FOREIGN KEY (id_pessoa) REFERENCES pessoas(id_pessoa),
    FOREIGN KEY (id_carona) REFERENCES carona(id_carona)
);

