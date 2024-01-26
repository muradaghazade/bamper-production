function filterContainers() {
    let input = document.getElementById('searchInput').value.toLowerCase();
    let containers = document.getElementsByClassName('grid-item');

    for (var i = 0; i < containers.length; i++) {
      let containerText = containers[i].innerText.toLowerCase();
  
      
      if (containerText.includes(input)) {
       
        containers[i].style.display = 'flex';
      } else {
        
        containers[i].style.display = 'none';
      }
    }
  }