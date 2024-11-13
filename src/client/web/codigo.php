<?php
    include('dbconfig.php');

    if(isset($_POST['salvar_contato']))
    {
        $nome = $_POST['nome'];
        $cpf = $_POST['cpf'];
        $placa = $POST['placa'];

        $post_data =
        [
            'CPF'=>$cpf,
            'Nome'=>$nome,
            'Placa'=>$placa,
        ];

        $ref_table = "Usuario";
        $post_result = $database->getReference($ref_table)->push($post_data);

        header('Location: index.php');
    }









?>
 