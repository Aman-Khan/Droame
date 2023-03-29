// Booking api will take customer information return booking detail with booking id
const bookingForm = document.querySelector('#drone-shot-booking');

bookingForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const customer_id = bookingForm.elements.customer_id.value;
  const location = bookingForm.elements.location.value;
  const datetime = bookingForm.elements.datetime.value;
  const drone_shot = bookingForm.elements.droneShotType.value;

  const booking = {
    customer_id,
    location,
    booked_for_time: datetime,
    drone_shot
  };


  const response = await fetch('http://127.0.0.1:8000/booking', { 
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(booking)
  });

  if (response.ok) {
    const bookingResponse = await response.json();
    alert('Slot Booked');

    // use bookingResponse for further operations
    console.log(bookingResponse);
    const bookingBloc = document.getElementById("booking-details");
    bookingBloc.innerHTML = `
    <b>Booking Id</b> : ${bookingResponse.booking_id}
    <br> <b>Customer Id</b> : ${bookingResponse.customer_id}
    <br> <b>Location</b> : ${bookingResponse.location}
    <br> <b>Event Time</b> : ${datetime}`;
    // Display response JSON body in innerHTML
  } else {
    response.json().then(data => {
      alert(`${response.status}. Error: ${data.detail}`);
    }).catch(() => {
      alert(`${response.status}.`);
    });
    console.log('Error occurred while booking drone shot.');
  }
});
