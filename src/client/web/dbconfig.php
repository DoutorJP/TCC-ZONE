<?php
    require __DIR__.'/vendor/autoload.php';

    use Kreait\Firebase\Factory;

    $factory = (new factory)
        ->withServiceAccount('keyFirebase.json')
        ->withDatabaseUri('https://dbteste-449d5-default-rtdb.firebaseio.com/');
    
    $database = $factory->createDatabase();
?>