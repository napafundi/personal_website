//Wait to run your initialization code until the DOM is fully loaded. This is needed
// when wanting to access elements that are later in the HTML than the <script>.
document.addEventListener('DOMContentLoaded', function(event) {;
    var modalBtn = document.getElementById("contactBtn");
    var modalView = document.getElementById("contactModal");
    var modalClose = document.getElementById("modalClose");
    var body = document.getElementById("mainContent");
    // display contactModal on link click
    modalBtn.onclick = function() {
        modalView.style.display = "block";
        body.className = ("mainContent blur-filter");
    }

    modalClose.onclick = function() {
        modalView.style.display = "none";
        body.className = ("mainContent");
    }

    window.onclick = function(event) {
        if (event.target == modalView) {
            modalView.style.display = "none";
            body.className = ("mainContent");
        }
    }
});

