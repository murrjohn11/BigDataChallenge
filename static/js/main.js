$('#btnRate').click(function(){
    $.ajax({
        url: '/getRate',
        type: 'POST',
        dataType: 'JSON',
        success: function(response){
            html = "<br>";
            $.each(response,function(){
               html += "Predicted Value:  " + this['value'] + "&nbsp&nbspDate and Time: " + this['month'] + " " + this['year']+ "<br>";
            });
            $('#prediction').html();
        },
        error: function(error){
            console.log(error)
        }
    });
});

$('#btnPredict').click(function(){
    $.ajax({
        url: '/predict',
        data: $('form').serialize(),
        type: 'POST',
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    });
});
