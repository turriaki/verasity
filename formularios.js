var name = document.getElementById("name").value;
var email = document.getElementById("email").value;
var message = document.getElementById("message").value;
var error_message = document.getElementById("error_message");

alert(name);
var name,
element = document.getElementById("name");
if (element != null) {
name = element.value;
}
else {
name = null;
}