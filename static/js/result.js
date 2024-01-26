let vin = document.getElementById('vin').innerText;

if (vin=="") {
    document.getElementById("full-result").innerHTML = `
    <header class="error-header">
    <div class="content">
        <img class="error-img" src="/static/images/404.jpg" alt="">
        
    </div>
    <h1 class="error-text">Axtardınız VIN üzrə nəticə tapılmadı</h1>
</header>
    `
}