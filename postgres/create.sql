CREATE TABLE IF NOT EXISTS public."dados_cadastrais" (
    "id" SERIAL PRIMARY KEY,
    "nome" VARCHAR(255) NOT NULL,
    "endereco" VARCHAR(255) NOT NULL,
    "telefone" VARCHAR(20) NOT NULL,
    "email" VARCHAR(255) NOT NULL
);
