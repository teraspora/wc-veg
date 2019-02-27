// Activation functions for Materialize

$(document).ready(function(){
  console.log("running jQuery activators...");
  // Activate side navigation for small screens:
  $('.sidenav').sidenav();

  // $('.button-collapse').sideNav({
  //     closeOnClick: true
  //   }
  // );

  // // Push alternate rows around:
  // $('.section .row:nth-of-type(2n+1) .col:last-of-type').addClass("offset-l1");

  // $('.section .row:nth-of-type(2n) .col:first-of-type').addClass("push-l7 offset-l1");

  // $('.section .row:nth-of-type(2n) .col:last-of-type').addClass("pull-l5 right-align offset-l1");

  // // Make image zoom on click:
  $('.materialboxed').materialbox();

  // // Activate 'parallax' scrolling:
  // $('.parallax').parallax();

  // // Activate tabs
  $('.tabs').tabs();
  
  // $('.collapsible').collapsible();
  
  $('select').formSelect();
  console.log("...Done!");
  
});