//ajax handling
var action = {
    //drive function
    Action: function (index) {
        $.ajax('http://192.168.1.43:8000/pi/app/tasks/' + index, {
            dataType: 'json',
            success: function (response) {
                console.log(response.description);
            },
            error: function (message) {
                console.log('error');
            }
        });
    },
    // gears function
    Gears: function (speed) {
        $.ajax('http://127.0.0.1:8000/pi/app/tasks/gear', {
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

// gear counter
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
                        $('#now_gear').html(currentGear);
                    } else {
                        currentGear = 5;
                        action.Gears(currentGear);
                    }
                    break;
                case 90:
                    //downshifting
                    if (currentGear > 0) {
                        currentGear--;
                        action.Gears(currentGear);
                        $('#now_gear').html(currentGear);
                    } else {
                        currentGear = 0;
                        action.Gears(currentGear);
                    }
                    break;
            }
        });
    } else {
        //button press function
        $('#forward').on('taphold', function () {
            action.Action(3);
        });
        $('#left').on('taphold', function () {
            action.Action(1);
        });
        $('#right').on('taphold', function () {
            action.Action(2);
        });
        $('#reverse').on('taphold', function () {
            action.Action(4);
        });
        //showing current gear
        $('#gear_up').on('taphold', function () {
            currentGear++;
            action.Gears(currentGear);
            $('#now_gear').html(currentGear);
        });
        $('#gear_down').on('taphold', function () {
            currentGear--;
            action.Gears(currentGear);
            $('#now_gear').html(currentGear);
        });
    }
});
