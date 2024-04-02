<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>TCC-ZONE</title>
</head>
<body>
   <header>
    <h1>TCC-ZONE</h1>
    <h2>Sistema integrado de monitoramento de estacionamentos privados</h2>
    </header>
    <hr>
    <form action="leitura.php" method="POST">
       <input type="radio" id="p_placa" name="busca" value="placa">
        <label for="p_placa">Consultar placa </label>
        <input type="text" name="campo_placa"  style="display:none;">
        <br>
        <input type="radio" id="p_nome" name="busca" value="nome">
        <label for="p_nome">Consultar nome</label>
        <input type="text" name="campo_nome">
        <input type="submit" value="Buscar">
    </form>
</body>
</html>