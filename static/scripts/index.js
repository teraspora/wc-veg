// Activation functions for Materialize

$(document).ready(function(){

  // Activate side navigation for small screens:
  $('.sidenav').sidenav();

  // // Push alternate rows around:
  // $('.section .row:nth-of-type(2n+1) .col:last-of-type').addClass("offset-l1");

  // $('.section .row:nth-of-type(2n) .col:first-of-type').addClass("push-l7 offset-l1");

  // $('.section .row:nth-of-type(2n) .col:last-of-type').addClass("pull-l5 right-align offset-l1");

  // // Make image zoom on click:
  // $('.materialboxed').materialbox();

  // // Activate 'parallax' scrolling:
  // $('.parallax').parallax();

  // // Activate tabs
  $('.tabs').tabs();
  
  // $('.collapsible').collapsible();
  
  $('select').formSelect();
  
});