$(document).ready(function() {
  $("#toggle-password-visibility-Btn").click(function() {
    console.log(this.value, "THISSS");
    let passwordInputDOM = document.getElementById("login-form-password");
    console.log(passwordInputDOM, "INPUT DOMM");
    if (this.getAttribute("value") == "hidden") {
      // change input type to text
      passwordInputDOM.type = "text";
      // change the icon to have the slash
      this.classList.remove("fa-eye");
      this.classList.add("fa-eye-slash");
      // changing the state of the toggle button
      this.setAttribute("value", "visible");
      
    } else if (this.getAttribute("value") == "visible") {
      // change the input type to password
      passwordInputDOM.type = "password";
      // change the icon to have the slash
      this.classList.remove("fa-eye-slash");
      this.classList.add("fa-eye");
      // changing the state of the toggle button
      this.setAttribute("value", "hidden");
    }
  });
  
});