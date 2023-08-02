<!DOCTYPE html>
<html>
<head>
    <title>Add Item to List on Click</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="add_item">Click here to add a new item to the list!</div>
    <ul class="my_list">
        <li>Existing Item 1</li>
        <li>Existing Item 2</li>
        <!-- Add more existing items here if needed -->
    </ul>

    <script>
        $(document).ready(function() {
            $('#add_item').click(function() {
                var newLiElement = $('<li>').text('Item');

                $('.my_list').append(newLiElement);
            });
        });
    </script>
</body>
</html>
