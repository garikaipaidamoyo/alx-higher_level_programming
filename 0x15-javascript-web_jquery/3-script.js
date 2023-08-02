<!DOCTYPE html>
<html>
<head>
    <title>Add Class to Header on Click</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="red_header">Click here to add the 'red' class to the header!</div>
    <header>
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
       $(document).ready(function() {
            $('#red_header').click(function() {
                 $('header').addClass('red');
            });
        });
    </script>
</body>
</html>
