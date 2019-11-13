$(document).ready(function(){
    /* Login function*/
    $('#login_button').click(function(){
        var username = $('#username').val();
        var password = $('#password').val();
        var role = $('#role').val();
        console.log('data>>',username,password,role)
        if((username == '') || (password == '') || (role == '')){
            $("#empty_fields_error").show().delay(5000).fadeOut();
        }else{
            console.log('start ajax here')
            $.ajax({
                 type: 'POST',
                 url: '/loginUser/',
                 data: {
                    'username':username,
                    'password':password,
                    'role':role
                 },
                 success: function(data) {    
                    console.log('data',data)
                    if(data.status == 'success'){
                        if(role=='admin'){
                            window.location.href='adminDashboard/'
                        }else{
                            window.location.href='agentDashboard/'
                        }  
                    }else{
                        $('#server_error').html(data.message);
                        $("#server_error").show().delay(5000).fadeOut();
                    }
                 },
                 failure: function(data) { 
                     alert('Got an error dude');
                 }
            });
        }
    })
})