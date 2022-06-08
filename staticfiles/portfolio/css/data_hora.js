function data_hora() {
    const horas = document.getElementById('Data_hora');
    let date = new Date();
    let h = date.getHours(); // 0 - 23
    let m = date.getMinutes(); // 0 - 59
    let s = date.getSeconds(); // 0 - 59

    h = (h < 10) ? "0" + h : h;
    m = (m < 10) ? "0" + m : m;
    s = (s < 10) ? "0" + s : s;

    horas.textContent = h + ":" + m + ":" + s;

    setTimeout(data_hora, 1000);
}
data_hora();