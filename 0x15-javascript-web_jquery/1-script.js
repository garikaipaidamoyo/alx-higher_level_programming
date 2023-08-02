<!DOCTYPE html>
<html>
<head>
    <title>Update Header Text Color with jQuery</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <header>
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
        // Wait for the document to be ready
        $(document).ready(function() {
            // Select the header element and change its text color to red (#FF0000)
            $('header').css('color', '#FF0000');
        });
    </script>
</body>
</html>
