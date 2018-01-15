// Morris.js Charts sample data for SB Admin template

var morrisBar;

$(document).ready(function(){
    var currentYear = 2017;
    var data_result = [];

    morrisBar = Morris.Bar({
            element: 'morris-area-chart',
            xkey: 'period',
            ykeys: ['Predicted','Actual'],
            labels: ['Predicted','Actual'],
            barRatio: 0.4,
            xLabelAngle: 35,
            hideHover: 'auto',
            resize: true
        });

    retrieveData(currentYear);

    $('#button-left').click(function(){
        currentYear = currentYear - 1;
        if(currentYear<1991) currentYear = 1991;
        retrieveData(currentYear);
    });

    $('#button-right').click(function(){
        currentYear = currentYear + 1;
        if(currentYear>2025) currentYear = 2025;
        retrieveData(currentYear);
    });


    $.post('/errors',function(response){
        $('#rsquared').html(response['rsquared']);
        $('#rmse').html(response['rmse']);
    },'JSON');

});

function retrieveData(currentYear){
    var result = [];

    $.post('/morris',{year:currentYear},function(response){
        $.each(response,function(){
            var member = {period: this['region'], Predicted: Math.ceil(this['value']),Actual: this['actual']};
            result.push(member);
        });
        morrisBar.setData(result);
    },'JSON');

    $('#year_result').html(currentYear);

}