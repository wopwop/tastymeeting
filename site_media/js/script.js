$(function(){
    

// Custom location select
    
if($('#location').length > 0)
{
$('#location').sbCustomSelect();    
}

// uniform html form elements
$("select, input:file, textarea, input:text, input:password").uniform();

if($('.tags').length > 0){
    $('.tags').tagsInput({
    'defaultText':'Ajouter un tag'
    });
}


// notification
if($("#notification").length > 0){
    $("#notification").animate({top:0},700,function(){
        setTimeout(function(){
             var outerHeight = $("#notification").outerHeight();
            $("#notification").animate({top:-outerHeight},700);
            },1500)
        })
}

// Facebook loginbox

$("#facebook_connect").live("click",function(){

    FB.login(function(response){
        if(response.session){
            if(response.perms){
                window.location = "/fbconnect";                
            } 
        }
        },{perms:'email'});

})


});

