// get the form and add an event listener for submit
const custSearch = document.getElementById("manage-customer-search");
custSearch.addEventListener("submit", function(event) {
  event.preventDefault(); // prevent default form submission

  // get the selected search option and value
  const searchOption = document.getElementById("search-options").value;
  const searchValue = document.getElementById("search-value").value;

  // get the token from session storage

  // make a fetch request to the API endpoint with token in the headers
  fetch(`http://127.0.0.1:8000/customer/details?search_option=${searchOption}&search_value=${searchValue}`, {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  })
    .then(response => {

      if (!response.ok) {
        throw new Error(`${response.status} - ${response.statusText}`);
      }
      return response.json();
    })
    .then(data => {
      // console.log(data)
      // update the inner HTML of the element with the fetched data
      const customerDetails = document.getElementById("customer-details");
      customerDetails.innerHTML = `<b>Customer ID</b> : ${data.customer_id}
       <br> <b>Name</b> : ${data.customer_name}
       <br> <b>Email</b> : ${data.customer_email}
       <br> <b>Phone No</b> : ${data.customer_name}`;
    })
    .catch(error => {
      // display an alert with the error details
      alert(`Error: ${error.message}`);
    });
});
