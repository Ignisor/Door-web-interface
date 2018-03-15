$(document).ready(function(){
    $('#open_button').click(function(){
        var btn = $(this);
        btn.text('...');

        $.post("/open/", {},
        function(data, status){
            if (status == "success" && data.success) {
                btn.css("background-color", "#43A047");
                btn.text("Opened");
                btn.attr("disabled", true);

                setTimeout(
                    function() {
                        btn.css("background-color", "");
                        btn.text("Open");
                        btn.removeAttr("disabled");
                    }, 5000);
            }
            else {
                btn.css("background-color", "#E53935");

                setTimeout(
                    function() {
                        btn.css("background-color", "");
                        btn.text("Open");
                    }, 200);
            }
        });
    });
});
