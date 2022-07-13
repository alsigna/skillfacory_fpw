// Задание 1.
// Напишите программу, которая работала бы следующим образом: в prompt вводится значение. 
// С помощью унарного плюса (арифметический оператор) необходимо преобразовать его в число,
// затем проверить с помощью typeof, принадлежит ли оно к множеству Number.
// Если это число, то вывести в консоль чётное оно или нечётное.
// Если передано не число, выведите: «Упс, кажется, вы ошиблись».
// *NaN, хоть и относится к типу Number, числом не является. Добавьте отдельную проверку для этого значения.

console.warn("==== TASK 1 ===");

let userInput = prompt("Введити число")

console.log("userInput = " + userInput)
userInput = +userInput

// всегда будет number, если строка введена, то будет NaN после унарного плюса
console.log("typeof result: " + typeof userInput)

let msg = ""
if (!isNaN(userInput)) {
    if (userInput % 2) {
        msg = "Нечетное число"
    } else {
        msg = "Четное число"
    }
} else {
    msg = "Упс, кажется, вы ошиблись."
}

console.log(msg)



// Задание 2.
// Дана переменная Х, которая может принимать любое значение.Написать программу,
// которая в зависимости от типа данных Х выводит в консоль сообщение вида: «X — число».
// Опишите три случая: когда х = числу, строке или логическому типу.
// В других случаях выводите сообщение: «Тип x не определён».

console.warn("==== TASK 2 ===");

const X = undefined

switch (typeof X) {
    case "boolean":
        console.log(X + " - логический тип")
        break;
    case "number":
        console.log(X + " - чиcло")
        break;
    case "string":
        console.log(X + " - строка")
        break;
    default:
        console.log("Тип " + X + " не определён")
        break;
}



// Задание 3.
// Дана строка. Необходимо вывести в консоль перевёрнутый вариант. Например, "Hello" -> "olleH".

console.warn("==== TASK 3 ===");

const strTask3 = "Hello";

function reverseString(str) {
    var splitString = str.split("");
    var reverseArray = splitString.reverse();
    return reverseArray.join("");
}
console.log(reverseString(strTask3))


// Задание 4.
// Записать в переменную случайное целое число в диапазоне [0; 100]. Используйте объект Math.

console.warn("==== TASK 4 ===");

function getRandom(max) {
    return Math.round(Math.random() * max)
}
const ans = getRandom(100)
console.log('ans :>> ', ans);

// Задание 5.
// Дан произвольный массив. Необходимо вывести количество элементов массива, затем перебрать его и
// вывести в консоль каждый элемент массива.

console.warn("==== TASK 5 ===");

const arr = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
console.log('arr.length :>> ', arr.length);

console.log("вариант 1")
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

console.log("вариант 2")
function show_arr_items(value, index) {
    console.log(`index: ${index} value: ${value}`)
}
arr.map(show_arr_items)

console.log("вариант 3")
arr.map(function (value, index) {
    console.log(`index: ${index} value: ${value}`)
})


// Задание 6.
// Дан массив. Проверить, одинаковые ли элементы в массиве и вывести результат true или false в консоль. 
// Речь идёт не о двух рядом стоящих одинаковых элементах, а обо всех. Проверить, все ли элементы в массиве одинаковые.

console.warn("==== TASK 6 ===");

function check_arr_items_eq(array) {
    for (let i = 1; i < array.length; i++) {
        if (array[i] !== array[i - 1]) {
            return false
        }
    }
    return true
}

let arr_task6 = [1, 1, 1, 1]
console.log('arr_task6 :>> ', arr_task6);
console.log(check_arr_items_eq(arr_task6))

arr_task6 = [1, 1, 2, 1]
console.log('arr_task6 :>> ', arr_task6);
console.log(check_arr_items_eq(arr_task6))



// Задание 7.
// Дан массив. Нужно вывести в консоль количество чётных и нечётных элементов в массиве.
// Если в массиве есть нулевой элемент, то он учитывается и выводится отдельно. 
// При выполнении задания необходимо учесть, что массив может содержать не только числа, но и, например, знаки, null и так далее.

console.warn("==== TASK 7 ===");

const arr_task7 = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, "5", "sd", NaN, null, Infinity, 5]
let odd = 0
let even = 0
let zero = 0

arr_task7.forEach(item => {
    if (typeof item === "number") {
        if (isNaN(item)) { // skip NaN
            return;
        } else if (!isFinite(item)) { // skip +/-Infinity
            return;
        };

        if (item === 0) {
            zero++;
        } else if (item % 2 === 0) {
            even++;
        } else {
            odd++;
        };
    };
});
console.log('arr_task7 :>> ', arr_task7);
console.log('even :>> ', even);
console.log('odd :>> ', odd);
console.log('zero :>> ', zero);



// Задание 8.
// Создайте произвольный массив Map.
// Получите его ключи и выведите в консоль все значения в виде «Ключ — Х, значение — Y».
// Используйте шаблонные строки.

console.warn("==== TASK 8 ===");

let fruits = new Map([
    ["apple", "green"],
    ["strawberry", "red"],
    ["blueberry", "blue"]
]);

for (const iterator of fruits) {
    console.log(`«Ключ — ${iterator[0]}, значение — ${iterator[1]}»`);
}