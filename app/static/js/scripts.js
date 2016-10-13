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

$(document).ready(function () {
    var mq = window.matchMedia("(max-device-width:800px)").matches;
    if (mq == true) {
        //key press function
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
            console.log(mq);
        });
    } else {
        //button press function
        $('#forward').on('taphold', function () {
            action.Action(3);
            console.log('sup sup');
        });
        $('#left').on('taphold', function () {
            action.Action(1);
            console.log('sup sup');
        });
        $('#right').on('taphold', function () {
            action.Action(2);
            console.log('sup sup');
        });
        $('#reverse').on('taphold', function () {
            action.Action(4);
            console.log('sup sup');
        });
        console.log(mq);
    }


});
