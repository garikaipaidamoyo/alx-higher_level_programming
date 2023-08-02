<!DOCTYPE html>
<html>
<head>
    <title>Update Header Text on Click</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="update_header">Click here to update the header text!</div>
    <header>
        <h1>Hello, this is a header!</h1>
    </header>

    <script>
        $(document).ready(function() {
            $('#update_header')
