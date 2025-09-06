// this is comment in javascript
console.log("hello world")
//; is optional in javascript

console.log(2+2)
console.log(2+4)
console.log(2/2)
console.log(2%4)

var age = 5
age = age + 1
console.log(age)

var xobject = {};
xObject = {
    name : "ankit",
    age : 99
}

// json - {
//     "name" : "ankit",
//     "age":31
// };

console.log(10<10);
console.log(10>10);
console.log(10==10);

var a = 10;
if(a >= 10) {
    console.log("A <10")
} else {
    console.log("a<10")
}

var a = 11;
if(a >= 10){
console.log("A >= 10")
}
else{
 console.log("A < 10")
}

function greet() {
    console.log("hi, how are you?")
}
greet()

// JSON -> JS Object (POstman Support JS oBJECT)`
// var response = '{"name":"ankit","age":"30", "cars":["audi","bmw","10"]};

var response = '{"name" : "Pramod","age" : 30,"cars" : ["Audi","BMW","I10"]}';


var parseResponseJS = JSON.parse(response)
console.log(parseResonJS["name"])

var parseResponseJS = JSON.parse(response)


console.log(parseResponseJS["name"])
console.log(parseResponseJS["age"])


// JS Object -> JSON

var jsObject = {
  name : "Amit",
  age : 89
}


var JSONStr = JSON.stringify(jsObject)
console.log(JSONStr)


var xArray = ["apple","organe","bananana"]
console.log(xArray[0])
console.log(xArray[1])
