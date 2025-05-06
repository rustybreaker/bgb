function startJourney() {
    document.querySelector('.container').style.display = 'none';
    document.getElementById('journey').style.display = 'block';
  }
  
  function nextStep() {
    document.getElementById('journey').style.display = 'none';
    document.getElementById('final').style.display = 'block';
  }
  