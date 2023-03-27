$(document).ready(function() {
    // Hide all containers initially
    $('.container.custom-width-65').children().hide();
  
    // Add click event listener to list items
    $('.list-group-item').click(function() {
      // Get the target container
      var target = $(this).data('target');
      
      // Hide all containers except the target
      $('.container.custom-width-65').children().not(target).hide();
      
      // Show the target container
      $(target).show();
    });
  });
  