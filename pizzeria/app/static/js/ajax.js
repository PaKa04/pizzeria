$(document).on('submit','#productform',function(e){
        e.preventDefault();
        $.ajax({
            type:'POST',
            url:'{% url "menu" %}',
            data:
            {
                user:$("#User").val(),
                product:$("#Nameofprod").val(),
                csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                  alert('Saved');
                    }
            })
        });
