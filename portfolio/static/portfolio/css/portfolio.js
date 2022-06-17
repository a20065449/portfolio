/* LEIRIA - Temperatura Atual*/

document.addEventListener('DOMContentLoaded', function() {
    let url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1100900.json';
    fetch(url)// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => {
                console.log(data);
                const tmax = data.data[0].tMax;
                const tmin = data.data[0].tMin;
        document.getElementById('Moeda').innerHTML = `Leiria  - Máx: ${tmax} - Min: ${tmin} `; // põe os dados na consola
    });
});


document.addEventListener('DOMContentLoaded', () => {
    let url = 'https://api.ipma.pt/open-data/distrits-islands.json';
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const locais = data.data;
            for (let local in locais) {
                let option = document.createElement('option');
                option.value = data.data[local].globalIdLocal;
                option.innerHTML = data.data[local].local;
                document.querySelector('#cidade').append(option);
            }

            document.querySelector('select').onchange = () => {
                const cidade = document.querySelector('#cidade').value;
                document.querySelector('#temperatura').innerHTML = `Teste -  ${cidade}`;
                console.log(cidade);
                return false;
            }
    });
});

/* API MOEDA*/
document.addEventListener('DOMContentLoaded', () => {

    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=feeea4a36c99c7c5f31c70dbfae3d215')
        .then(response => response.json())
        .then(data => {
            const rates = data.rates;
            for (let rate in rates) {
                let option = document.createElement('option');
                option.value = rate;
                option.innerHTML = rate;
                document.querySelector('#moeda').append(option);
            }

            document.querySelector('select').onchange = () => {

                const moeda = document.querySelector('#moeda').value;
                const frase = `1 Eur = ${rates[moeda].toFixed(2)} ${moeda}`;
                document.querySelector('#cambio').innerHTML = frase;

                return false;
            }
        });
});

