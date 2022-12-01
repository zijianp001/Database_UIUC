$(document).ready(function () {
    $('#editcpudialog').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const content = button.data('content') // Extract info from data-* attributes
        console.log(content)
        const copy = content.replaceAll('\'', '"')

        const modal = $(this)
        const myjson = JSON.parse(copy)
        for (item in myjson) {
            modal.find('#edit'+item).val(myjson[item]);
        }
    })

    $('#login_btn').click(function () {
        var userid = $('.login').find("#username");
        var psword = $('.login').find("#psword");
        $.ajax({
            type: 'POST',
            url: '/check',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'userid': userid[0].value,
                'password': psword[0].value
            }),
            success: function () {
                window.location.href = "/";
            },
            error: function () {
                alert("Incorrect password or Account does not exist!!")
                console.log('Error');
            }
        })
    })

    $('#register_btn').click(function () {
        var userid = $('.id').find("input");
        var psword = $('.pw').find("input");
        var cfmpsword = $('.cpw').find("input");
        // console.log(userid[0].value)
        // console.log(psword[0].value)
        // console.log(cfmpsword[0].value)
        if (psword[0].value != cfmpsword[0].value)
            alert("Password not consistent!")
        else {
            $.ajax({
                type: 'POST',
                url: '/createid',
                contentType: 'application/json;charset=UTF-8',
                data: JSON.stringify({
                    'userid': userid[0].value,
                    'password': psword[0].value,
                    'confirmpw': cfmpsword[0].value
                }),
                success: function () {
                    location.reload();
                    alert("Registration Success!!")
                },
                error: function () {
                    alert("User ID already exist!!")
                    console.log('Error');
                }
            })
        }
    })

    $('#show_cpu').click(function () {
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

    $('#show_ram').click(function () {
        $.ajax({
            type: 'POST',
            url: '/ram',
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
        // console.log($('.content').find('#adquery1_input').val());
        console.log(JSON.stringify({
            'input': $('.content').find('#adquery1_input').val(),
        }));
        $.ajax({
            type: 'POST',
            url: '/ADquery',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'input': $('.content').find('#adquery1_input').val()
            }),
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });

    $('#ADquery1_sp').click(function () {
        // console.log($('.content').find('#adquery1_input').val());
        console.log(JSON.stringify({
            'input': $('.content').find('#adquery1_input_sp').val(),
        }));
        $.ajax({
            type: 'POST',
            url: '/ADquerysp',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'input': $('.content').find('#adquery1_input_sp').val()
            }),
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
            data: JSON.stringify({
                'input': $('.content').find('#adquery2_input').val()
            }),
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });

    $('#ADquery2_sp').click(function () {
        console.log(JSON.stringify({
            'input': $('.content').find('#adquery2_input_sp').val(),
        }));
        $.ajax({
            type: 'POST',
            url: '/ADquery2sp',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'input': $('.content').find('#adquery2_input_sp').val()
            }),
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        })
    });


    $('#submit-task').click(function () {
        var list = $('#addcpudialog').find(".addcpu").children("input");
        console.log(list[1].value);
        var result = '';
        result += '{';
        for(var i = 0; i < list.length; i++) {
            result += '"';
            result += i + 1;
            result += '"';
            result += ':'
            result += '"';
            result += list[i].value;
            result += '"';
            if(i != list.length - 1)
                result += ',';
        }
        result += '}';
        console.log(result);

        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: result,
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
                alert("Error, please check you input data");
            }
        });
    });


    $('#submit-edit').click(function () {
        var list = $('#editcpudialog').find(".editcpu").children("input");
        var result = '';
        result += '{';
        for(var i = 0; i < list.length; i++) {
            result += '"';
            result += i + 1;
            result += '"';
            result += ':'
            result += '"';
            result += list[i].value;
            result += '"';
            if(i != list.length - 1)
                result += ',';
        }
        result += '}';
        console.log(result);
        $.ajax({
            type: 'POST',
            url: '/edit',
            contentType: 'application/json;charset=UTF-8',
            data: result,
            success: function (res) {
                $("body").html(res);
            },
            error: function () {
                console.log('Error');
            }
        });
    });
});