// Import jQuery and Bootstrap JavaScript
import $ from 'jquery';
import 'bootstrap';

// When the DOM is ready
$(function() {

  // Collapse the navbar when a link is clicked
  $('.navbar-nav>li>a').on('click', function(){
    $('.navbar-collapse').collapse('hide');
  });

});
