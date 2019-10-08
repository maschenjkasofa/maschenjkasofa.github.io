var expectedUserLogin = 'npi'
var expectedUserPassword = '123456'

//get user's date
var userName = prompt("Enter your login");
var userPassword = prompt("Enter your password");

/*
Check if user's entered date are equal to expected
*/
if(expectedUserLogin == userName && expectedUserPassword == userPassword) {
    alert("Welcome to our web site!!!")
}
else {
    //remove body element
    var e = document.body;
    e.parentNode.removeChild(e);
}