<!DOCTYPE html>
<html>
<head>
    <title>Update Header Text Color</title>
</head>
<body>
    <header>
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var headerElement = document.querySelector('header');
            headerElement.style.color = '#FF0000';
        });
    </script>
</body>
</html>
