document.addEventListener("DOMContentLoaded", function () {
  const movingDiv = document.querySelector(".moving-image");
  const images = [
    "/static/images/pic1.png",
    "/static/images/pic2.png",
    "/static/images/pic3.png",
  ];

  let index = 0;

  setInterval(() => {
    index = (index + 1) % images.length;
    movingDiv.style.backgroundImage = `url('${images[index]}')`;
  }, 3000); // change image every 3 seconds
});
