const form = document.querySelector('#reg-form');
// const token = sessionStorage.getItem('token');
const operator_id = sessionStorage.getItem('operator_id');
document.getElementById('operator-id').textContent = getOperatorId;

const formData = new FormData(form);
formData.append('operator_id', operator_id);

console.log("hello world")
console.log(formData.get('operator_id'))

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  formData.append('operator_id', operator_id);

  const requestBody = {};
  formData.forEach((value, key) => requestBody[key] = value);
  requestBody['country_code'] = '91';

  try {
    const response = await fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    });

    const data = await response.json();
    if (response.status !== 201) {
        alert(`Error: ${response.status} - ${data.detail}`);
    }
    else{
        alert(`Successfully Registrated - ${response.status}`);
        // Clear the form
        form.reset();
        populateRecentCustomersTable();   // quick access recent customer table reload to render new registration 
    }
    console.log(data);
  } catch (error) {
    console.error(error);
  }

});
