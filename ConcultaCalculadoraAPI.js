function Calcular(){

    let tipo = document.getElementById('tipo').value;
    let numero = document.getElementById('numero').value;
    let base = document.getElementById('base').value;
    const apiUrl = "YourLocalHost/calcular/"+numero+"/"+base+"/"+tipo;

    // Chama a API usando a Fetch API
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao chamar a API: ' + response.status);
            }
            return response.json();
        })
        .then(data => {
            let valorResult = document.getElementById('result');
            valorResult.textContent = (data);
        })
        .catch(error => {
            console.error('Erro:', error);
        });
}