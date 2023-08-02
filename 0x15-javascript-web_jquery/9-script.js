<!DOCTYPE html>
<html>
<head>
    <title>Fetch and Display Translation</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="hello">Translation will appear here</div>

    <script>
        $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
            var translation = data.hello;
            $('#hello').text(translation);
        });
    </script>
