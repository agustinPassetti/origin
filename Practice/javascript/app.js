//Uso de variables
/*
var nombre = 'agus';
console.log(nombre);
console.log(typeof(nombre));

var edad = 26;
console.log(edad);
console.log(typeof(edad));

edad = 'cinco';
console.log(edad);
console.log(typeof(edad));

var sueldo = 35000.12;
console.log(sueldo);
console.log(typeof(sueldo));

var tieneTrabajo = false;
console.log(tieneTrabajo);
console.log(typeof(tieneTrabajo));

var puestoDeTrabajo;
console.log(puestoDeTrabajo);
    puestoDeTrabajo = null;
    console.log(puestoDeTrabajo);

**********************************/

/**********
 * Operadores Matematicos + - * /
 


 var edadAna, edadMaria, diferenciaEdad;
 var sumaEdades, yearAna, yearMaria, yearActual;

 edadAna = 34;
 edadMaria = 28;
 yearActual = 2019;

 diferenciaEdad = edadAna - edadMaria;
 sumaEdades = edadAna + edadMaria;

 yearAna = yearActual - edadAna;
 yearMaria = yearActual - edadMaria;

 console.log(diferenciaEdad);
 console.log(sumaEdades);
 console.log('Año en que nació Ana ' + yearAna);
 console.log('Año en que nació María ' + yearMaria);
 console.log(yearActual * 5);
 console.log(yearActual / 2);

*/


/****
 * Operadores Lógicos unarios y de asignación
 
// Lógicos < > <= >= ==

var edadAna, edadMaria, diferenciaEdad;
edadAna = 34;
edadMaria = 28;

var mayorAna =! (edadAna == edadMaria);
console.log(mayorAna);

// Unarios, ++incremento, --decremento

//edadAna ++;
console.log(edadAna--);
console.log(edadAna);

//Asignacion, += -=, *= /=, %=

var a = 12;
var b = 5;

var c = a % 5;
console.log(c);
a += b;
console.log(a);
*/

/********
 * Sentencia if...else
 
var nombre= 'agus';
var esCasado = false;

if (esCasado == true){
    console.log(nombre + ' es casado.');
}else {
    console.log (nombre + ' es soltero.')
}

// If anidado

var nombre = 'Agus';
var edad = 67;

// edad < 12 en un niño
//edad > 11, es menor que 18, es un adolescente
// edad > 17, < a 60, es adulto
//edad > 60 es anciano

if (edad < 12){
    console.log(nombre + ' es un niño');
}else if((edad > 11) &&(edad < 18)){
    console.log(nombre + ' es un adolescente');
}else if((edad > 17) && (edad < 60)){
    console.log(nombre + ' es un adulto');
}else {
    console.log(nombre + ' es un anciano')
}


//Switch

var mes = 4;

switch(mes){
    case 1:
        console.log('enero');
        break;
    case 2:
        console.log('febrero');
        break;
    case 3:
        console.log('marzo');
        break;
    case 4:
        console.log('abril');
        break;
    default:
        console.log('Mes no encontrado.');
}


// Sentencia For

for (var i = 5; i <= 25; i+=5){
    console.log(i);
}



// Sentencia While, do while

var i = 10;
while(i >= 1){
    console.log(i);
    i--;
}
console.log(i);



//Sentencia Do while (si o si se ejecuta una vez)

var i = 101;
do{
    console.log(i);
    i++;
}while(i <= 10);

console.log(i);

*/









