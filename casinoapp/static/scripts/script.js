$(document).ready(function() {
    var promo_carousel_index = 0;

    ShowCurrentPromoOnly(promo_carousel_index);
    console.log(promo_carousel_index);

    function ShowCurrentPromoOnly(promo_index) {
        // get the 'rail' element
        let rails = document.querySelector('.sliding-promo-rails');

        // unshow all promos except current promo
        for (let i=0; i<rails.children.length; i++) {
            console.log(rails.children[i])
            if (i != promo_index) {
                rails.children[i].style.display = "none";
            }
        }
    }

    $("#nav-user-profile").click(function() {
        // dropdown not shown, at the time of click
        if (this.getAttribute('visible') == "false") {
            // show the dropdown
            let dropdown = document.getElementById("nav-up-dropdown");
            console.log(dropdown);
            dropdown.style.display = "flex";
            dropdown.style.zIndex = "2";
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
            dropdown.style.top = "0%";
//            dropdown.style.display = "none";

            // change the dropdown arrow direction
            let dd_arrow = document.getElementById("nav-up-dd-arrow");
            dd_arrow.style.transform = "rotate(0deg)";
            // change the visible attribute to false
            this.setAttribute('visible', 'false');
        }

    });

    $("#sp-prev-arrow").click(function() {
        // get the 'rail' element
        let rails = document.querySelector(".sliding-promo-rails");
        let promo_wrapper = document.querySelector(".sliding-promo-wrapper");
        console.log(rails.children);
        console.log(rails.children.length);

        if (promo_carousel_index > 0) {
            promo_wrapper.style.width = "200%";

            // show the previous promo. (promo is offscreen at this point)
            let prev_promo = rails.children[promo_carousel_index - 1];
            prev_promo.style.display = "flex";

            rails.style.transform = `translateX(${-50}%)`;

            // decrement the carousel index
            promo_carousel_index--;

            return
            // move the carousel to show the next promo
            rails.style.transform = `translateX(${promo_carousel_index * -50}%)`;

            return

            setTimeout(function() {
                rails.style.transition = "unset";
                // unshow the current promo
                let current_promo = rails.children[promo_carousel_index + 1];
                current_promo.style.display = "none";

                promo_wrapper.style.width = "100%";
                rails.style.transform = "translateX(0%)";

                setTimeout(()=>{rails.style.transition = "1s ease"}, 100);

            },1000);
        }
    });

    $("#sp-next-arrow").click(function() {
        // get the 'rail' element
        let rails = document.querySelector(".sliding-promo-rails");
        let promo_wrapper = document.querySelector(".sliding-promo-wrapper");
        console.log(rails.children);
        console.log(rails.children.length);

        if (promo_carousel_index < rails.children.length-1) {
            promo_wrapper.style.width = "200%";

            // show the next promo. (promo is offscreen at this point)
            let next_promo = rails.children[promo_carousel_index + 1];
            next_promo.style.display = "flex";

            // increment the carousel index
            promo_carousel_index++;

            // move the carousel to show the next promo
            rails.style.transform = `translateX(${1 * -50}%)`;

            setTimeout(function() {
                rails.style.transition = "unset";
                // unshow the current promo
                let current_promo = rails.children[promo_carousel_index - 1];
                current_promo.style.display = "none";

                promo_wrapper.style.width = "100%";
                rails.style.transform = "translateX(0%)";

                setTimeout(()=>{rails.style.transition = "1s ease"}, 100);

            },1000);
        }

    });


});