let a = 7;
let b = 94;
/*
let aux;
aux = a;
a = b;
b = aux;
*/
[a, b] = [b, a];

console.log(a);
console.log(b);