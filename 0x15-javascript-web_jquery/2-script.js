<!DOCTYPE html>
<html>
<head>
    <title>Update Header Text Color on Click</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="red_header">Click here to change the header text color to red!</div>
    <header>
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
       $(document).ready(function() {
           $('#red_header').click(function() {
               $('header').css('color', '#FF0000');
            });
        });
    </script>
</body>
</html>
