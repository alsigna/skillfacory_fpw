let msg = "hello from script"
console.log(msg)

var a;
a = 4

var b = a + 2

console.log(b)
// age = prompt("enter number")
// result = age * 4
// alert("your result is " + result)
console.log(typeof a)
// document.addEventListener()

console.log(Boolean([123]));
console.log(Boolean(""));

console.log(0 || NaN);

const k = 1
const w = 3
if (k + w > 4) {
    console.log("if")
} else {
    console.log("else")
}

// =====

let firstName = "Ivan";
let result = `${firstName} glad to see you!`;
console.log(result);

// =====

let firstName1 = 'Ivan';
let lastName1 = 'Ivanov';
function getFullName(strings, firstNameExp, lastNameExp) {
    let str0 = strings[0];// "My  first name is " 
    let str1 = strings[1]; // " and the last " 
    return `${str0}${firstNameExp}${str1}${lastNameExp}`;
}
let result1 = getFullName`My first name is ${firstName1} and the last ${lastName1}`;
console.log(result1);

// =====

function template(strings, ...keys) {
    return (function (...values) {
        var dict = values[values.length - 1] || {};
        var result = [strings[0]];
        keys.forEach(function (key, i) {
            var value = Number.isInteger(key) ? values[key] : dict[key];
            result.push(value, strings[i + 1]);
        });
        return result.join('');
    });
}

var t1Closure = template`${0}${1}${0}!`;
console.log(t1Closure('Y', 'A'));  // "YAY!"
var t2Closure = template`${0} ${'foo'}!`;
console.log(t2Closure('Hello', { foo: 'World' }));  // "Hello World!"

// =====

const str_len = "str_len"
console.log(str_len.length)
console.log(str_len.toUpperCase())
console.log(str_len.slice(1, 5))

// =====
// const strLove = "I love JS";
const strLove = "I learn JS";
let strLoveRes;
if (strLove.includes(" love ")) {
    strLoveRes = strLove.toUpperCase();
} else {
    strLoveRes = strLove.toLowerCase();
}
console.log(strLoveRes)