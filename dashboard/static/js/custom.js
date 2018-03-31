//JS validation for fields of signup and login page page
// Validation for username field
let elem = document.querySelector("#username");
elem.addEventListener('blur', function(evt){
if(elem.value === "")
{
    //empty value is empty
    let dv = document.querySelector("#username-div");
    let allClasses = dv.classList;
    allClasses.add("has-error");
    allClasses.remove("has-success");
    }
    else
    { //when it has value
    let dv = document.querySelector("#username-div");
    let allClasses = dv.classList;
    allClasses.remove("has-error");
    allClasses.add("has-success");
    }});
//validation for name field
let nm = document.querySelector("#name");
nm.addEventListener('blur', function(evt){
if(nm.value === "")
{
    //empty value is empty
    let dvv = document.querySelector("#name-div");
    let allClasses = dvv.classList;
    allClasses.add("has-error");
    allClasses.remove("has-success");
    }
    else
    { //when it has value
    let dvv = document.querySelector("#name-div");
    let allClasses = dvv.classList;
    allClasses.remove("has-error");
    allClasses.add("has-success");
    }});
//validation for email field
let el = document.querySelector("#email");
el.addEventListener('blur', function(evt){
if(el.value === "")
{
    //empty value is empty
    let d = document.querySelector("#email-div");
    let allClasses = d.classList;
    allClasses.add("has-error");
    allClasses.remove("has-success");
    }
    else
    { //when it has value
    let d = document.querySelector("#email-div");
    let allClasses = d.classList;
    allClasses.remove("has-error");
    allClasses.add("has-success");
    }});
//validation for password field
let ele = document.querySelector("#password");
ele.addEventListener('blur', function(evt){
if(ele.value === "")
{
    //empty value is empty
    let ddv = document.querySelector("#password-div");
    let allClasses = ddv.classList;
    allClasses.add("has-error");
    allClasses.remove("has-success");
    }
    else
    { //when it has value
    let ddv = document.querySelector("#password-div");
    let allClasses = ddv.classList;
    allClasses.remove("has-error");
    allClasses.add("has-success");
    }});