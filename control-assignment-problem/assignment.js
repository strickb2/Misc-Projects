const randomNumber = Math.random(); // produces random number between 0 (including) and 1 (excluding)

if (randomNumber > 0.7) {
    alert("The number is " + randomNumber);
}

array = [1, 2, 3]
let j = 0;

for (let i = 0; i <= 2; i++) {
    console.log(array[i]);
}

do {
    console.log(array.length - j);
    j++;
} while (j < 3);

const randomNumber2 = Math.random();

if (randomNumber2 > 0.7 && randomNumber > 0.7 || randomNumber < 0.2 || randomNumber2 < 0.2) {
    alert("Both are greater than 0.7 or One of the two is not greater than 0.2");
}