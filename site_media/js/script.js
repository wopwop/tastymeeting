$(function(){
   
   // custom selectbox for home page
   $("#location").sbCustomSelect();
   
   // change event
   $(".sb-select").change(function(){
      alert("d");
   })
});