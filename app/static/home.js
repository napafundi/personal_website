//display modal for image clicked
function modalDisplay(obj) {
    var imgId = obj.id;
    var modalId = imgId + "_modal";
    var modalImgId = modalId + "_img";
    var captionId = obj.id + "_caption";
    var modal = document.getElementById(modalId);
    var modalImg = document.getElementById(modalImgId);
    var caption = document.getElementById(captionId);
    modal.style.display = "block";
    modalImg.src = obj.src;
    caption.innerHTML = obj.alt;
}