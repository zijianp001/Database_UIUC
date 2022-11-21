$(document).ready(function () {
    var current = ""
    $('#editcpudialog').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const ProductId = button.data('source') // Extract info from data-* attributes
        const content = button.data('content') // Extract info from data-* attributes
        const copy = content.replaceAll('\'', '"')

        const modal = $(this)
        //console.log(ProductId);
        const myjson = JSON.parse(copy)
        for (item in myjson) {
            modal.find('#'+item).val(myjson[item]);
        }
    })


    $('#show_cpu').click(function () {
        current = 'cpu'
        $.ajax({
            type: 'POST',
            url: '/cpu',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    })

    $('#show_gpu').click(function () {
        console.log(current);
        current = 'gpu'
        $.ajax({
            type: 'POST',
            url: '/gpu',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    })

    $('#show_mob').click(function () {
        $.ajax({
            type: 'POST',
            url: '/mob',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    })


    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response);
                // location.reload();
                $("body").html(res);
            },
            error: function () {
                console.log('Error delete failed');
            }
        });
    });


    $('.search').click(function () {
        var current;
        if ($('.checkbox').find('#MotherBoard').is(':checked') == true)
            current = 'MOB';
        else if ($('.checkbox').find('#GPU').is(':checked') == true) 
            current = 'GPU';
        else if ($('.checkbox').find('#RAM').is(':checked') == true)
            current = 'RAM';
        else 
            current = 'CPU';
        
        console.log(current);
        console.log(JSON.stringify({
            'input': $('.container').find('#livebox').val(),
            'current': current
        }));
        $.ajax({
            type: 'POST',
            url: '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'input': $('.container').find('#livebox').val(),
                'current': current
            }),
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });


    $('#ADquery1').click(function () {
        $.ajax({
            type: 'POST',
            url: '/ADquery',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });

    $('#ADquery2').click(function () {
        $.ajax({
            type: 'POST',
            url: '/ADquery2',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });


    $('#submit-task').click(function () {
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
                console.log(res.response);
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('#submit-edit').click(function () {
        $.ajax({
            type: 'POST',
            url: '/edit',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                '1': $('#editcpudialog').find('#ProductId').val(),
                '2': $('#editcpudialog').find('#BrandName').val(),
                '3': $('#editcpudialog').find('#ProductName').val(),
                '4': $('#editcpudialog').find('#CodeName').val(),
                '5': $('#editcpudialog').find('#Cores').val(),
                '6': $('#editcpudialog').find('#Clock').val(),
                '7': $('#editcpudialog').find('#CPUSocket').val(),
                '8': $('#editcpudialog').find('#CPUProcess').val(),
                '9': $('#editcpudialog').find('#L3_Cache').val(),
                '10': $('#editcpudialog').find('#TDP').val(),
                '11': $('#editcpudialog').find('#ReleaseYear').val()
            }),
            success: function (res) {
                console.log(res.response);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});