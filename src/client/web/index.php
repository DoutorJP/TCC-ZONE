<!doctype html>

<html lang="en">

  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="3">
    <title>Teste do Zone-TCC</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>

  <body>

    <div class="py-4">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">

                        <div class="card-header">
                            <h4>
                                <b>
                                    Entradas do Sistema
                                </b>
                            </h4>
                        </div>

                        
                        <div class="card-body">
                                <table class="table table-bordered table-striped">
                                    <thead>
                                        <tr>
                                            <th>#</th>
                                            <th>Data </th>
                                            <th>Nome do proprietário </th>
                                            <th>Placa do veículo </th>
                                            <th>Modelo do carro</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <?php
                                            include('dbconfig.php');

                                            $ref_table = 'Carros';
                                            $fetchData = $database->getReference($ref_table)->getValue();

                                            
                                            if($fetchData > 0){ //retornou algo
                                                $hash = 1;
                                                foreach($fetchData as $key => $row){
                                        ?>
                                                    <tr>
                                                        <td><?=$hash++?></td>
                                                        <td><?=$row['DataEntrada']?></td>
                                                        <td><?=$row['Dono']?></td>
                                                        <td><?=$row['Placa']?></td>
                                                        <td><?=$row['Modelo']?></td>
                                                    </tr>
                                        <?php
                                                }
                                            }
                                            else{
                                        ?>
                                                <tr>
                                                    <td colspan ="7">Nenhum entrada de dados no momento.</td>
                                                </tr>
                                        <?php
                                            }
                                        ?>
                                    </tbody>
                                </table>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="py-4">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="card">
                        <div class="card-header">
                            <h4>
                                <b>
                                    Usuários Cadastrados
                                </b>
                            </h4>
                        </div>
                        <div class="card-body">
                        <table class="table table-bordered table-striped">
                                    <thead>
                                        <tr>
                                            <th>Proprietário</th>
                                            <th>CPF</th>
                                            <th>Carros</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                    <?php
                                            include('dbconfig.php');

                                            $ref_table = 'Usuario';
                                            $fetchData = $database->getReference($ref_table)->getValue();


                                            if($fetchData > 0){ //retornou algo
                                                $hash = 1;
                                                foreach($fetchData as $key => $row){
                                                    $placas = $row['Placas'];
                                                    
                                                    


                                        ?>
                                                    <tr>
                                                        <td><?=$row['Nome']?></td>
                                                        <td><?=$row['CPF']?></td>
                                                        <td>
                                                            <?php
                                                                foreach($placas as $p => $placa){
                                                            
                                                                    echo $placa;
                                                                    if($p < count($placas)-1){
                                                                        echo ", ";
                                                                    }

                                                                }
                                                                                                                            
                                                            ?>
                                                        </td>
                                                    </tr>
                                        <?php
                                                }
                                            }
                                            else{
                                        ?>
                                                <tr>
                                                    <td colspan ="7">Nenhum entrada de dados no momento.</td>
                                                </tr>
                                        <?php
                                            }
                                        ?>
                                    </tbody>
                                </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>

</html>