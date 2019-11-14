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
                            $('#email').val('');
                            $('#password').val('');
                            $('#role').val('');
                            $('#f_name').val('');
                            $('#l_name').val('');
                            $('#phone').val('');
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


    //Add Locations
    var locations_arr = []
    $('#add_location_btn').click(function(){
        var location_state = $('#location_state').val();
        var timezone = $('#timezone-offset').val();
        var company_address = $('#company_address').val();
        var location_type = $('#location_type').val();
        console.log('location>>>',location_state,timezone,company_address,location_type)
         if((location_state == '') || (timezone == '') || (company_address == '') || (location_type == '')){
            $("#emptymodel_fields_error").show();
            setTimeout(function() {
                $("#emptymodel_fields_error").fadeOut('fast')
            }, 3000);
        }else{
            var location_json = {'location_state':location_state, 'timezone':timezone,
            'company_address':company_address, 'location_type':location_type}
            locations_arr.push(location_json)
            console.log('added',locations_arr)
            $("#success_add_location").show();
            setTimeout(function() {
                $("#success_add_location").fadeOut('fast')
            }, 3000);
            $('#company_address').val('');
            $('#location_type').val('');
        }
    })


    //Add Personnel
    var personnel_arr = []
    $('#add_personnel_btn').click(function(){
        var first_name = $('#first_name').val();
        var last_name = $('#last_name').val();
        var personnel_email = $('#personnel_email').val();
        var personnel_location = $('#personnel_location').val();
        console.log('location>>>',first_name,last_name,personnel_email,personnel_location)
         if((first_name == '') || (last_name == '') || (personnel_email == '') || (personnel_location == '')){
            $("#emptypersonnel_fields_error").show();
            setTimeout(function() {
                $("#emptypersonnel_fields_error").fadeOut('fast')
            }, 3000);
        }else{
            var valid_email = validateEmail(personnel_email)
            if(valid_email==true){
                var personnel_json = {'first_name':first_name, 'last_name':last_name,
                'personnel_email':personnel_email, 'personnel_location':personnel_location}
                personnel_arr.push(personnel_json)
                console.log('added',personnel_arr)
                $("#success_add_personnel").show();
                setTimeout(function() {
                    $("#success_add_personnel").fadeOut('fast')
                }, 3000);
                $('#first_name').val('');
                $('#last_name').val('');
                $('#personnel_email').val('');
                $('#personnel_location').val('');
            }else{
                $("#personnel_invalid_email").show();
                setTimeout(function() {
                    $("#personnel_invalid_email").fadeOut('fast')
                }, 3000);
            }
            
        }
    })


    //Create New Account
    $('#create_client_account').click(function(){
        //Customer Details
        var client_name = $('#client_name').val();
        var client_id = $('#client_id').val();
        var switch_id = $('#switch_id').val();

        //Address
        var street_address = $('#street').val();
        var city = $('#city').val();
        var state = $('#state').val();
        var zip = $('#zip').val();

        //Work
        var start_day = $('#start_day').val();
        var end_day = $('#end_day').val();
        var start_time = $('#start_timepicker').val();
        var end_time = $('#end_timepicker').val();

        //Locations
        var locations = locations_arr;

        //Personnel
        var personnels = personnel_arr

        //Instructions
        var instructions = $('textarea#instructions').val();


        console.log('values>>>',client_name,client_id,switch_id,street_address,city,state,zip,
            start_day,end_day,start_time,end_time,locations,personnels,instructions
            )
        if((client_name == '') || (client_id == '') || (switch_id == '') || (street_address == '') 
            || (city == '') || (state == '') || (zip == '') || (start_day == '') || 
            (end_day == '') || (start_time == '') || (end_time == '') || (locations == '') 
            || (personnels == '') || (instructions == '')){
            $("#emptytabs_fields_error").show();
            setTimeout(function() {
                $("#emptytabs_fields_error").fadeOut('fast')
            }, 3000);
        }else{
            console.log('start ajax here')
            $.ajax({
             type: 'POST',
             url: '/createClientAccount/',
             data: {
                'client_name':client_name,
                'client_id':client_id,
                'switch_id':switch_id,
                'street_address':street_address,
                'city':city,
                'state':state,
                'zip':zip,
                'start_day':start_day,
                'end_day':end_day,
                'start_time':start_time,
                'end_time':end_time,
                'locations':locations,
                'personnels':personnels,
                'instructions':instructions,

             },
             success: function(data) {    
                console.log('data',data)
                // if(data.status == 'success'){
                //     $("#success_message").show()
                //     setTimeout(function() {
                //         $("#success_message").hide('blind', {}, 500)
                //     }, 3000);
                // }else{
                //     $('#server_error').html(data.message);
                //     $("#server_error").show()
                //     setTimeout(function() {
                //         $("#server_error").hide('blind', {}, 500)
                //     }, 3000);
                // }
             },
             failure: function(data) { 
                 alert('Got an error dude');
             }
        });
        }

    })

    //Restrict input field to numbers only
    $('input[name="zip_code"]').keyup(function(e)                        {
      if (/\D/g.test(this.value))
      {
        // Filter non-digits from input value.
        this.value = this.value.replace(/\D/g, '');
      }
    });
    
    // Restrict input fields to text only

    $( "#first_name" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    $( "#last_name" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });
    $( "#city" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

    $( "#state" ).keypress(function(e) {
        var key = e.keyCode;
        if (key >= 48 && key <= 57) {
            e.preventDefault();
        }
    });

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