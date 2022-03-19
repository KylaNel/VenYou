$("#nav-1 a").on("click", function() {
    var position = $(this).parent().position();
    var width = $(this).parent().width();
    $("#nav-1 .slide1").css({ opacity: 1, left: +position.left, width: width });
  });
  
  $("#nav-1 a").mouseover(function() {
    var position = $(this).parent().position();
    var width = $(this).parent().width();
    $("#nav-1 .slide2").css({ 
      opacity: 1, left: +position.left, width: width }).addClass("squeeze");
  });
  
  $("#nav-1 a").on("mouseout", function() {
    $("#nav-1 .slide2").css({ opacity: 0 }).removeClass("squeeze");
  });

  var currentWidth = $("#nav-1").find("li:nth-of-type(3) a").parent("li").width();
  var current = $("li:nth-of-type(3) a").position();