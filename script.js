$(function(){
	var btn_click=0;
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

	$("body").on("click","input[class='downbutton']",function(e,sub){
	            e.preventDefault();
	        var id=$(this).attr("id");
	        sub=-1;
	        var value=$('[name="'+id+'"]').val();

	        var counter=parseInt(value,10)+sub;
	        if(counter < 0){
	            counter=0;
	        }
	        $('[name="'+id+'"]').val(counter);

	});

	$('body').on('click','#sort_btn',function(e){
		        e.preventDefault();
		        btn_click+=1;
		        dictionary={};
		        dictionary['click']=btn_click;
		        $('#nrml tr:gt(1)').each(function(index,element){
		            var first=$(this).find('td').eq(2).html();
		            var count_id=$(first).attr("id");
		            var value=$('[name="'+count_id+'"]').val();
		            dictionary[count_id]=value;
		        });
		        $.ajax({
		                url:'/sorting',
		                type:'POST',
		                data:dictionary,
		                success: function(response){
		                    $('#ajaxresponse').html(response);
		                },
		                error: function (error) {
		                    console.log(error);

		                }


		        });

    	});

  

});