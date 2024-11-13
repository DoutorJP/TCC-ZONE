<?php
    include('dbconfig.php');
?>
 
 <!DOCTYPE html>
 <html lang="en">
 <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <title>Zone - Cadastro de Usuário</title>
 </head>
 <body>
    <div class="py-4">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-header">
                            <h4>
                                Cadastro de Usuário
                            </h4>
                        </div>

                        <div class="card-body">
                            <form action="codigo.php" method="POST">

                                <div class="form-group mb-3">
                                    <label for="">Nome</label>
                                    <input type="text" name="nome" class="form-control">
                                </div>
                                <div class="form-group mb-3">
                                    <label for="">CPF</label>
                                    <input type="text" name="cpf" class="form-control">
                                </div>
                                <div class="form-group mb-3">
                                    <label for="">Placa</label>
                                    <input type="text" name="placa" class="form-control">
                                </div>
                                <div class="form-group mb-3">
                                    <button type="submit" name="salvar_contato" class="btn btn-primary">Cadastrar</button>
                                </div>
                            </form>

                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
 </body>
 </html>