// Herencia, Encapsulamiento, Polimorfismo, Abstracion 

class Persona {
    nombre = "";
    apellido = "";
    genero = "";

    comer = function(){
        return "Funcion Comer de Persona";
    }

    correr = function(){
        return "Funcion Correr de Persona";
    }

    nombreCompleto = function(){
        return this.nombre + " " + this.apellido;
    }

    constructor(nombre = "John", apellido = "Doe", genero = "M"){
        this.nombre = nombre;
        this.apellido = apellido;
        this.genero = genero;
    }

}
 
class Estudiante extends Persona {
    
    estudios = "";

    constructor(nombre = "John", apellido = "Doe", genero = "M", estudios = "Ninguno"){
        super(nombre, apellido, genero);
        this.estudios = estudios
    }

}

let persona_1 = new Persona();
persona_1.nombre = "Luis"
persona_1.apellido = "Rodriguez";

let persona_2 = new Persona();
persona_2.nombre = "Alejandra";
persona_2.apellido = "Salas"

let estudiante_1 = new Estudiante();
estudiante_1.nombre = "Pedro";
estudiante_1.apellido = "Perez";

console.log(persona_1.nombreCompleto());
console.log(persona_2.nombreCompleto());
console.log(estudiante_1.nombreCompleto());