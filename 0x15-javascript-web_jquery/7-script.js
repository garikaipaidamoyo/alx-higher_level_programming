<!DOCTYPE html>
<html>
<head>
    <title>Fetch Character Name</title>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
<body>
    <div id="character">Character Name Will Appear Here</div>

    <script>
       $(document).ready(function() {
            $(setJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
               var characterName = data.name;
                
                $('#character').text(characterName);
            });
        });
    </script>
</body>
</html>
