function validate(e) {
    e.preventDefault();

    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const age = document.getElementById("age").value;
    const msgbox = document.getElementById("message");

    let message = " ";

    if (email === "") {
        message = "Enter an email";
        msgbox.style.color = "red";
    } else if (pass === "") {
        message = "Enter a password";
        msgbox.style.color = "red";
     } else if (age === "") {
        message = "Enter your age";
        msgbox,style.color = "red" ;
     } else  {
        message = "Log in successfull!";
        msgbox,style.color = "green" ;
    }

    msgbox.innerHTML = message;
     
}

