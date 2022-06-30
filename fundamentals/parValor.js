// par nome/valor
const saudacao = 'Opa' // contexto léxico 1

function exec(){
    const saudacao = 'Falaaa' // contexto léxico 2
    return saudacao
}

// Objetos são grupos aninhados de pares nome/valor
const cliente = {
    nome: 'Hector',
    idade: 19,
    peso: 55,
    endereco: {
        logradouro: 'Rua Projetada Norte Sul 02',
        numero: 2053
    }
}
console.log(saudacao)
console.log(exec())
console.log(cliente)