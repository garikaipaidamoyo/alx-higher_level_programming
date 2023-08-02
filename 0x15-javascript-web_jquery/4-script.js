<!DOCTYPE html>
<html>
<head>
    <title>Toggle Class on Header Click</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="toggle_header">Click here to toggle the class of the header!</div>
    <header class="red">
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
        $(document).ready(function() {
             $('#toggle_header').click(function() {
                var headerElement = $('header');

                headerElement.toggleClass('red green');
            });
        });
    </script>
</body>
</html>
