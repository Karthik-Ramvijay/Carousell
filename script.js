$(function(){

	$('#Submit_Topic').click(function(e) {
                e.preventDefault();
            var txt = $('#topictxt').val();
            if($.trim(txt)== ''){
                alert("Topic Field cannot be Empty");
                return false;
            }
             else
            {

                $.ajax({
                    url: '/',
                    type: 'POST',
                    data: $('form').serialize(),

                    success: function (response) {
                        $('#topictxt').val('');
                        $('#nrml tr:last').after(response);

                    },

                    error: function (error) {
                        console.log(error);
                    }

                });
            }

    });
    
});