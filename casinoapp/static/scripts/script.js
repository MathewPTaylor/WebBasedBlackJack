$(document).ready(function() {
    $("#nav-user-profile").click(function() {
        // dropdown not shown, at the time of click
        if (this.getAttribute('visible') == "false") {
            // show the dropdown
            let dropdown = document.getElementById("nav-up-dropdown");
            console.log(dropdown);
            dropdown.style.zIndex = "4";
            dropdown.style.display = "flex";
            dropdown.style.top = "100%";

            // change the dropdown arrow direction
            let dd_arrow = document.getElementById("nav-up-dd-arrow");
            dd_arrow.style.transform = "rotate(180deg)";

            // change the visible attribute to true
            this.setAttribute('visible', 'true');

        // dropdown is shown, at the time of click
        } else if (this.getAttribute('visible') == "true") {
            // unshow the dropdown

            let dropdown = document.getElementById("nav-up-dropdown");
            console.log("dropdown" + dropdown);
            dropdown.style.zIndex = "-1";
            dropdown.style.display = "none";
            dropdown.style.top = "0%";

            // change the dropdown arrow direction
            let dd_arrow = document.getElementById("nav-up-dd-arrow");
            dd_arrow.style.transform = "rotate(0deg)";
            // change the visible attribute to false
            this.setAttribute('visible', 'false');
        }

    });

});