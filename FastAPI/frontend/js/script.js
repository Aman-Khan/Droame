// index page scrip for login as operator and redirect to operator page
const loginButton = document.querySelector('.btn-primary');
const operatorIdInput = document.querySelector('.form-control');

loginButton.addEventListener('click', () => {
  const operatorId = operatorIdInput.value;
  fetch('http://127.0.0.1:8000/login', {  //post request to login API to fectch JWT token
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ operator_id: operatorId })
  })
  .then(response => {
    if (response.ok) {
      return response.json();
    } else {
      throw new Error('Invalid credentials');
    }
  })
  .then(data => {
    const { token } = data;

    // storing token and operator id for future use in authentication and for other use 
    sessionStorage.setItem('token', token); 
    sessionStorage.setItem('operator_id', operatorId);
    window.location.href = 'operator.html'; // navigate to the operaton page
  })
  .catch(error => {
    console.error(error);
    alert('Invalid Credentials.');
  });
});

