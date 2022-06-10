
/*
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://api.exchangeratesapi.io/v1/latest?access_key=feeea4a36c99c7c5f31c70dbfae3d215')// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => {
            const rate = data.rates.USD;
            document.getElementById('Moeda').innerHTML = `1 EUR = ${rate.toFixed(2)} USD`; // põe os dados na consola
    });
});

/*
 */

document.addEventListener('DOMContentLoaded', function() {
    let url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1100900.json';
    fetch(url)// envia GET request ao URL
        .then(response => response.json()) // Põe a responsta no formato json
        .then(data => {
                console.log(data);
                const country = data.country;
                const tmax = data.data[0].tMax;
                const tmin = data.data[0].tMin;
                console.log(country);
                console.log(tmax);
        document.getElementById('Moeda').innerHTML = `Temperatura - Máxima: ${tmax} - Minima: ${tmin} `; // põe os dados na consola
    });
});


/*
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
