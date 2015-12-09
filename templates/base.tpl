<!DOCTYPE html>
<html class="no-js">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>Persona Generator</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width">

        <link rel="stylesheet" href="static/css/bootstrap.css">
        <link rel="stylesheet" href="static/css/main.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
        
        <script src="static/js/vendor/modernizr-2.6.2.min.js"></script>
    </head>
    <body>
        {% include 'persona.tpl' with context %}
        
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="static/js/vendor/jquery-1.10.2.min.js"><\/script>')</script>
        <script src="static/js/vendor/bootstrap.min.js"></script>
        <script src="static/js/main.js"></script>
    </body>
</html>
