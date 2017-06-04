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
	
    $("body").on("click","input[class='upbutton']", function(e,add){
			e.preventDefault();
        var id=$(this).attr("id");
        add=1;
        var value=$('[name="'+id+'"]').val();
        var counter=parseInt(value,10)+add;
        if(counter < 0){
            counter=0;
        }
        $('[name="'+id+'"]').val(counter);

	});

  

});