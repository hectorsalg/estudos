const palavra = "H3ctor"

console.log(palavra.charAt(5))
console.log(palavra.charAt(6))
console.log(palavra.charCodeAt(1))
console.log(palavra.indexOf("3"))

console.log(palavra.substring(1))
console.log(palavra.substring(0, 3))

console.log("palavra ".concat(palavra).concat("!"))
console.log("palavra " + palavra + "!")
console.log(palavra.replace(/\d/, 'e'))

console.log("hec, salg, alves".split(', '))
