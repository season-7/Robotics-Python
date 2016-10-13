/*ajax handling*/
var action = {
    Action: function (index) {
        $.ajax('http://192.168.1.43:8000/pi/app/tasks/' + index, {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').html(message);
                console.log('error');
            }
        });
    },
    Gears: function (speed) {
        $.ajax('http://192.168.1.43:8000/pi/app/tasks/gear', {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
                console.log(currentGear);
            },
            error: function (message) {
                $('#response').html(message);
                console.log(currentGear);
            },
            data: {
                currentGear: currentGear
            }
        });
    }
};
/*speed handling*/
//default gear
var currentGear = 0;

$(document).ready(function () {
    //media query function
    var mq = window.matchMedia("(max-device-width:800px)").matches;
    if (mq === false) {
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
                case 65:
                    //upshifting
                    if (currentGear < 5) {
                        currentGear++;
                        action.Gears(currentGear);
                        alert(currentGear);
                    } else {
                        currentGear = 5;
                        action.Gears(currentGear);
                        alert(currentGear);
                    }
                    break;
                case 90:
                    //downshifting
                    if (currentGear > 0) {
                        currentGear--;
                        action.Gears(currentGear);
                        alert(currentGear);
                    } else {
                        currentGear = 0;
                        action.Gears(currentGear);
                        alert(currentGear);
                    }
                    break;
            }
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
    }
});
