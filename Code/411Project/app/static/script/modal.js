
$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error delete failed');
            }
        });
    });


    $('.search').click(function () {
        var keyword = $('.container').find('#livebox').val();
        console.log(keyword);
        $.ajax({
            type: 'POST',
            url: '/search/' + keyword,
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        })
    });


    $('#submit-task').click(function () {
        console.log($('#addcpudialog').find('#pid').val())
        console.log($('#addcpudialog').find('#bnm').val())
        console.log($('#addcpudialog').find('#pnm').val())
        console.log($('#addcpudialog').find('#cnm').val())
        console.log($('#addcpudialog').find('#cor').val())
        console.log($('#addcpudialog').find('#clo').val())
        console.log($('#addcpudialog').find('#cso').val())
        console.log($('#addcpudialog').find('#cpr').val())
        console.log($('#addcpudialog').find('#l3c').val())
        console.log($('#addcpudialog').find('#tdp').val())
        console.log($('#addcpudialog').find('#ryr').val())

        console.log(typeof(JSON.stringify({
            '1': $('#addcpudialog').find('#pid').val(),
            '2': $('#addcpudialog').find('#bnm').val(),
            '3': $('#addcpudialog').find('#pnm').val(),
            '4': $('#addcpudialog').find('#cnm').val(),
            '5': $('#addcpudialog').find('#cor').val(),
            '6': $('#addcpudialog').find('#clo').val(),
            '7': $('#addcpudialog').find('#cso').val(),
            '8': $('#addcpudialog').find('#cpr').val(),
            '9': $('#addcpudialog').find('#l3c').val(),
            '10': $('#addcpudialog').find('#tdp').val(),
            '11': $('#addcpudialog').find('#ryr').val()
        })));
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                '1': $('#addcpudialog').find('#pid').val(),
                '2': $('#addcpudialog').find('#bnm').val(),
                '3': $('#addcpudialog').find('#pnm').val(),
                '4': $('#addcpudialog').find('#cnm').val(),
                '5': $('#addcpudialog').find('#cor').val(),
                '6': $('#addcpudialog').find('#clo').val(),
                '7': $('#addcpudialog').find('#cso').val(),
                '8': $('#addcpudialog').find('#cpr').val(),
                '9': $('#addcpudialog').find('#l3c').val(),
                '10': $('#addcpudialog').find('#tdp').val(),
                '11': $('#addcpudialog').find('#ryr').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});