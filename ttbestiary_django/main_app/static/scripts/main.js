$(".navbar-burger").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");
  });

$(".navbar-burger-bottom").click(function () {
    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger-bottom").toggleClass("is-active");
    $(".navbar-menu-bottom").toggleClass("is-active");
  });

$(".rollable").click(function () {
  console.log(Math.floor(Math.random()*20)+1)
})