$(document).ready(function(){
    /* Create New Agent Function*/
    $('#create_agent_button').click(function(){
        var email = $('#email').val();
        var password = $('#password').val();
        var role = $('#role').val();
        var f_name = $('#f_name').val();
        var l_name = $('#l_name').val();
        var phone = $('#phone').val();
        console.log('data>>',email,password,role,f_name,l_name,phone)
        if((email == '') || (password == '') || (role == '') || (f_name == '') || (l_name == '') || (phone == '')){
            $("#empty_fields_error").show();
            setTimeout(function() {
                $("#empty_fields_error").fadeOut('fast')
            }, 3000);
        }else{
            var valid_email = validateEmail(email);
            console.log('>>',valid_email)
            if(valid_email == true){
                console.log('start ajax here')
                $.ajax({
                     type: 'POST',
                     url: '/createNewAgent/',
                     data: {
                        'email':email,
                        'password':password,
                        'role':role,
                        'f_name':f_name,
                        'l_name':l_name,
                        'phone':phone
                     },
                     success: function(data) {    
                        console.log('data',data)
                        if(data.status == 'success'){
                            $("#success_message").show()
                            setTimeout(function() {
                                $("#success_message").hide('blind', {}, 500)
                            }, 3000);
                        }else{
                            $('#server_error').html(data.message);
                            $("#server_error").show()
                            setTimeout(function() {
                                $("#server_error").hide('blind', {}, 500)
                            }, 3000);
                        }
                     },
                     failure: function(data) { 
                         alert('Got an error dude');
                     }
                });
            }else{
                $("#invalid_email_error").show()
                setTimeout(function() {
                    $("#invalid_email_error").hide('blind', {}, 500)
                }, 3000);
            }
        
        }
    })


    //Create New Account
    
    
    // Restrict input fields to text only
    $( "#f_name" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    $( "#client_name" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    $( "#l_name" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    $( "#role" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    //Validate Email
    function validateEmail($email) {
      var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/;
      return emailReg.test( $email );
    }

    //Validate Phone Number
    function validatePhone($txtPhone) {
        var filter = /^((\+[1-9]{1,4}[ \-]*)|(\([0-9]{2,3}\)[ \-]*)|([0-9]{2,4})[ \-]*)*?[0-9]{3,4}?[ \-]*[0-9]{3,4}?$/;
        if (filter.test($txtPhone)) {
            return true;
        }
        else {
            return false;
        }
    }

})