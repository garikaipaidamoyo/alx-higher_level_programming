<!DOCTYPE html>
<html>
<head>
    <title>List Movies</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <ul id="list_movies">
        <!-- Movie titles will be listed here -->
    </ul>

    <script>
        $(document).ready(function() {
            $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
                var movies = data.results;

                $.each(movies, function(index, movie) {
                    var movieTitle = movie.title;
                    var listItem = $('<li>').text(movieTitle);
                    $('#list_movies').append(listItem);
                });
            });
        });
    </script>
</body>
</html>
