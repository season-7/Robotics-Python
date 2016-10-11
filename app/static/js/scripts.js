// var responseFunc = function (resp) {
//     var message = $('<p></p>');
//     message.append(resp.description);
//     console.log(resp.description);
//     $('#response').hide().html(message).fadeIn();
// };

var action = {
    leftAction: function () {
        $.ajax('http://192.168.1.48:8000/pi/app/tasks/1', {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').append().html(message);
                console.log('new');
            }
        });
    },
    rightAction: function () {
        $.ajax('http://192.168.1.48:8000/pi/app/tasks/2', {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').append().html(message);
                console.log('new');
            }
        })
    },
    forwardAction: function () {
        $.ajax('http://192.168.1.48:8000/pi/app/tasks/3', {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').append().html(message);
                console.log('new');
            }
        })
    },
    reverseAction: function () {
        $.ajax('http://192.168.1.48:8000/pi/app/tasks/4', {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').append().html(message);
                console.log('new');
            }
        })
    }
};

$(document).ready(function() {
    // alert("Hello World");
	$(document).on('keydown', function (e) {
	    switch (e.keyCode) {
            case 37:
                action.leftAction();
                break;
            case 38:
                action.forwardAction();
                break;
            case 39:
                action.rightAction();
                break;
            case 40:
                action.reverseAction();
                break;
        }

    });
});
