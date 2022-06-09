document.addEventListener('DOMContentLoaded', function() {
    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=feeea4a36c99c7c5f31c70dbfae3d215')// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => {
            const rate = data.rates.USD;
            document.getElementById('Moeda').innerHTML = `1 EUR = ${rate.toFixed(2)} USD`; // põe os dados na consola
    });
});

/*
document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.ipma.pt/open-data/distrits-islands.json')// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => console.log(data));
});
*/

/*

document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1100900.json')// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => {
            const tMax = data.tMax;
            console-log(tMax);
            for (let tem)
            document.getElementById('Moeda').innerHTML = `Temperatura Maxima = ${tMax} `; // põe os dados na consola
    }); // põe os dados na consola
});

document.addEventListener('DOMContentLoaded', () => {

    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=feeea4a36c99c7c5f31c70dbfae3d215')
        .then(response => response.json())
        .then(data => {
            const rates = data.rates;
            console.log(rates);
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

    */
