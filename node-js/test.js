function Student(name='', age=0) {
    this.name = name;
    this.age = age;
}

var stud1 = new Student('Vikash', 22)
var stud2 = new Student('Danesh', 54)
var stud3 = new Student('Sugar')

// console.log(stud1.name);
// console.log(stud1.age);

// console.log(stud2.name);
// console.log(stud2.age);

// console.log(stud3.name);
console.log(stud3.age);

const moviePartons = [
    {name: 'Pete', age: 23},
    {name: 'Sarah', age: 18},
    {name: 'Ashely', age: 65},
    {name: 'Prashant', age: 90},
    {name: 'Lweis', age: 46},
    {name: 'OPw', age: 5},
    stud1,
    stud2,
    stud3
]

// moviePartons.forEach(function(parton) {
//     console.log(`${parton.name}`)
// })

const showName = (inforamtion) => {console.log(`Dis ur name?: ${inforamtion}`)}

// moviePartons.forEach(parton => console.log(parton.name))
moviePartons.forEach(parton => showName(parton.name))

const legalPatron = moviePartons.filter((patron) => {return patron.age < 18;})

const movieMap = moviePartons.map((parton) => {
    return {
        firstName: "Stenaly", 
        yearsOnMars: parton.age, 
        isLegal: parton.age > 18 ? true : false
    }
})

console.log(movieMap)

// console.log(legalPatron)

// for (let index = 0; index < moviePartons.length; index++) {
//     console.log(moviePartons[index].name)
// }

const testJSON = JSON.stringify(moviePartons)

// console.log(testJSON)