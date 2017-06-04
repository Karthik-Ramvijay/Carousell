$(function(){

	$('#Submit_Topic').click(function(e) {
                e.preventDefault();
            var txt = $('#topictxt').val();
            if($.trim(txt)== ''){
                alert("Topic Field cannot be Empty");
                return false;
            }

    });
});