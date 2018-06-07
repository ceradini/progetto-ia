window.addEventListener('load', removeBanner, false);

function removeBanner(){
  wait(200);
  $('.tb-site').remove();
  $('#av_toolbar_iframe').remove();
}

function wait(ms){
   var start = new Date().getTime();
   var end = start;
   while(end < start + ms) {
     end = new Date().getTime();
  }
}