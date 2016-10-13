//speed handling
//gear variable
var gears = [1, 2, 3, 4, 5];
//ajax handling
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
    },
    Gears: function (speed) {
        $.ajax('http://192.168.1.35:8000/pi/app/tasks/gear' {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                $('#response').html(message);
                console.log('error');
            },
            data: {
                currentGear: currentGear
            }
        });
    };
};

//gear logic
var currentGear = 0;
var gearCounter = 0;
$(document).ready(function () {
    //keypress speed
    $(document).on("keydown", function (w) {
        switch (w.keyCode) {
            case 65:
                //upshifting
                if (currentGear < gears.length) {
                    currentGear = gears[gearCounter] + gears[gearCounter + 1];
                } else {
                    currentGear = gears[4];
                }
                break;
            case 90:
                //downshifting
                if (currentGear > gears[0]) {
                    currentGear = gears[gearCounter] + gears[gearCounter - 1];
                } else {
                    currentGear = 0;
                }
                break;
        }
    });

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
