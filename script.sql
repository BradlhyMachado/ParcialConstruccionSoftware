CREATE TABLE grupousuario (
    id_grupo INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_grupo VARCHAR(20) NOT NULL
);

CREATE TABLE usuario (
    dni INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    telefono VARCHAR(9) NOT NULL,
    correo VARCHAR(50) NOT NULL,
    contrasena VARCHAR(50) NOT NULL,
    id_grupo INT NOT NULL,
    FOREIGN KEY (id_grupo) REFERENCES grupousuario(id_grupo)
);

CREATE TABLE profesor (
    id_profesor INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    asignatura_profesor VARCHAR(50) NOT NULL,
    dni INT NOT NULL,
    FOREIGN KEY (dni) REFERENCES usuario(dni)
);

CREATE TABLE curso (
    id_curso INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_curso VARCHAR(50) NOT NULL
);

CREATE TABLE seccion (
    id_seccion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    nombre_seccion VARCHAR(10) NOT NULL,
    id_curso INT NOT NULL,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

CREATE TABLE profesorseccion (
    id_profesor INT NOT NULL NOT NULL AUTO_INCREMENT,    
    id_seccion INT NOT null,
    PRIMARY KEY (id_profesor, id_seccion),
    FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor),
    FOREIGN KEY (id_seccion) REFERENCES seccion(id_seccion)
);

CREATE TABLE Horario (
    id_horario INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    dia_semana VARCHAR(10) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    id_seccion INT NOT NULL,
    FOREIGN KEY (id_seccion) REFERENCES seccion(id_seccion)
);

CREATE TABLE Asistencia (
    id_asistencia INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fecha DATE NOT NULL,
    hora_entrada TIME NOT NULL,
    hora_salida TIME NOT NULL,
    dni INT NOT NULL,
    id_horario INT NOT NULL,
    FOREIGN KEY (dni) REFERENCES usuario(dni),
    FOREIGN KEY (id_horario) REFERENCES Horario(id_horario)
);

CREATE TABLE Estudiante (
    id_estudiante INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    dni INT NOT NULL,
    FOREIGN KEY (dni) REFERENCES usuario(dni)
);

CREATE TABLE Participacion (
    id_participacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    fecha DATE NOT NULL,
    nota_final DECIMAL(4,2) NOT NULL,
    id_horario INT NOT NULL,
    FOREIGN KEY (id_horario) REFERENCES Horario(id_horario)
);

CREATE TABLE Matricula (
    id_matricula INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_estudiante INT NOT NULL,
    semestre VARCHAR(10) NOT NULL,
    carrera VARCHAR(50),
    estado BOOL NOT null,
    id_seccion INT NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiante(id_estudiante),
    FOREIGN KEY (id_seccion) REFERENCES seccion(id_seccion)
);

CREATE TABLE Justificacion (
    id_justificacion INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_asistencia INT UNIQUE,
    razon VARCHAR(50) NOT NULL,
    estado BOOL,
    FOREIGN KEY (id_asistencia) REFERENCES Asistencia(id_asistencia)
);
