-- Host: localhost    Database: homestead
-- ------------------------------------------------------

--
-- Table structure for table "user"
--

DROP TABLE IF EXISTS "user";
CREATE TABLE "user" (
  id SERIAL PRIMARY KEY,
  first_name varchar(30) NOT NULL,
  last_name varchar(30) NOT NULL,
  email varchar(255) NOT NULL UNIQUE,
  password varchar(128) NOT NULL,
  created_date timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
  last_update timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL
);

--
-- Dumping data for table "user"
--

INSERT INTO "user" VALUES (1,'Admin','User','admin@gmail.com','$6$rounds=1024000$phcQ98tCIJFO/RS/$IGScys.VJRNHqfYXvdlbgJUJtlmKcaTx7oS4KaJj2USmgTdMj8wFCBJgn9ilHOGLFkigkI1rOD9jOO964PD001','2022-06-21 17:09:04','2022-06-21 17:09:04');

-- Dump completed on 2022-06-21 18:09:20
