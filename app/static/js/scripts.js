// var responseFunc = function (resp) {
//     var message = $('<p></p>');
//     message.append(resp.description);
//     console.log(resp.description);
//     $('#response').hide().html(message).fadeIn();
// };

var action = {
    Action: function (index) {
        $.ajax('http://192.168.1.35:8000/pi/app/tasks/' + index, {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').html(message);
                console.log('error');
            }
        });
    }
};

$(document).ready(function() {
    // alert("Hello World");
	$(document).on('keydown', function (e) {
	    switch (e.keyCode) {
            case 37:
                action.Action(1);
                break;
            case 38:
                action.Action(3);
                break;
            case 39:
                action.Action(2);
                break;
            case 40:
                action.Action(4);
                break;
        }

    });
});
