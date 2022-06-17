/* LEIRIA - Temperatura Atual*/

document.addEventListener('DOMContentLoaded', function() {
    let url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1100900.json';
    fetch(url)
        .then(response => response.json())
        .then(data => {
                console.log(data);
                const tmax = data.data[0].tMax;
                const tmin = data.data[0].tMin;
        document.getElementById('Moeda').innerHTML = `Leiria  - Máx: ${tmax} - Min: ${tmin} `;
    });
});


document.addEventListener('DOMContentLoaded', () => {
    let url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1100900.json';
    fetch(url)
        .then(response => response.json())
        .then(data => {

            const chuva = data.data[0].precipitaProb;
            const tmax = data.data[0].tMax;
            const tmin = data.data[0].tMin;
            const hoje = data.data[0].forecastDate;


            document.getElementById('chuva').innerHTML = `Probabilidade de Percipitação: ${chuva}`;
            document.getElementById('hoje').innerHTML = `Data: ${hoje}`;
            document.getElementById('max').innerHTML = `Máxima: ${tmax}`;
            document.getElementById('min').innerHTML = `Minima: ${tmin}`;
            /*
            const locais = data.data;
            for (let local in locais) {
                let option = document.createElement('option');
                option.value = data.data[local].forecastDate;
                option.innerHTML = data.data[local].forecastDate;
                document.querySelector('#cidade').append(option);
            }
            document.querySelector('select').onchange = () => {
                const cidade = document.querySelector('#cidade').value;
                const frase = `Possibilidade de Chuva = ${data.data[cidade].precipitaProb} `;
                document.getElementById('#temperatura').innerHTML = frase;
                return false;
            }
             */
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

