CREATE DATABASE IF NOT EXISTS "NOTES";
USE "NOTES";

CREATE TABLE "tblUsuario" (
    "IdUsuario" serial NOT NULL,
    "Nombre" varchar(100),
    "Apellido" varchar(300),
    "Email" varchar(250) NOT NULL,
    "Contraseña" varchar(100) NOT NULL,
    "FechaAuditoria" timestamp NOT NULL,
    CONSTRAINT "pk_tblUsuario" PRIMARY KEY ("IdUsuario"),
    CONSTRAINT "uq_email" UNIQUE("Email") 
);

CREATE TABLE "tblNota"(
    "IdNota" serial NOT NULL,
    "IdUsuario" int NOT NULL,
    "TituloNota" varchar(255) NOT NULL,
    "Contenido" text,
    "FechaAuditoria" timestamp NOT NULL,
    CONSTRAINT "pk_tblNota" PRIMARY KEY ("IdNota"),
    CONSTRAINT "FK_tblNota_tblUsuario" FOREIGN KEY ("IdUsuario") REFERENCES "tblUsuario"("IdUsuario")
);