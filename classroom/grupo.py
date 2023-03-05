from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo ordinado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
 
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
            return "Grupo de estudiantes: grupo predeterminado"
        else:
            return "Grupo de estudiantes: " + self._grupo
    
    def getGrado(self):
        return "Grado"+self.grado
    
    def setGrado(self, grado):
        self.grado = grado

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
        
    @ classmethod
    def getNombre(cls):
        return cls.nombre
