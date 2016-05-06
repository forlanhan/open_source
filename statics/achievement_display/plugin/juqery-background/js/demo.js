/**
 * Particleground demo
 * @author Jonathan Nicol - @mrjnicol
 */

$(document).ready(function() {
  $('#search-main').particleground({
    dotColor: '#5cbdaa',
    lineColor: '#7EC0EE'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});