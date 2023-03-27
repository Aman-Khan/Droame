const loginButton = document.querySelector('.btn-primary');
const operatorIdInput = document.querySelector('.form-control');

loginButton.addEventListener('click', () => {
  const operatorId = operatorIdInput.value;
  fetch('http://127.0.0.1:8000/login', {
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
    sessionStorage.setItem('token', token);
    sessionStorage.setItem('operator_id', operatorId);
    window.location.href = 'operator.html'; // navigate to the home page
  })
  .catch(error => {
    console.error(error);
    alert('Invalid Credentials.');
  });
});
