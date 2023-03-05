from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=[], listadoAlumnos=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = listadoAlumnos
 
    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def __str__(self):
        if self._grupo:
            self._grupo = "grupo predeterminado"
            return "Grupo de estudiantes: " + self._grupo
        else:
            return "Grupo de estudiantes: " + self._grupo
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
        
