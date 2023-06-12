#!/usr/bin/node
const no = Math.floor(Number(process.argv[2]));
console.log(isNaN(no) ? 'Not a number' : `My Number: ${no}`);
