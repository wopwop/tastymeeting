$(function(){
    

// Custom location select
    
if($('#location').length > 0)
{
$('#location').sbCustomSelect();    
}

// display loginbox in lightbox

if($('#lightbox').length > 0){
    jQuery('#lightbox').lightbox();
}


// Facebook loginbox

$("#facebook_connect").live("click",function(){

    FB.login(function(response){
        if(response.session){
            if(response.perms){
                
                FB.api('/me', function(response) {
                     $("#fullName").val(response.first_name+" "+response.last_name);
                     $("#email").val(response.email);
                });

                
            } 
        }
        },{perms:'email'});

})


});

