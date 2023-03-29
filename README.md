<h4> How to Run (Droame) Web-Application </h4>
  <ul>
    <li><a href="https://github.com/Aman-Khan/Droame"> Clone this repo</a></li>
    <li>Setup Python Virtual Environment(not necessary)</li>
    <li>Install all <a href="https://github.com/Aman-Khan/Droame/blob/main/Web-Application/requirement.txt">requirement</a> from requirements.txt file</li>
    <li>Run uvicorn app.main:app --reload or uvicorn app.main:app to start API services</li>
    <li>Register operator by using operator signup API</li>
    <li>Run any live server to host index.html web page</li>
    <li>Use the Opertor id which use signup earlier to login</li>
    <li>After redirecting on operator.html page you can perform operator operations</li>
   </ul>
   
<h4>Signup API body (JSON)</h4>
<p>http://127.0.0.1:8000/signup</p>
<code>{
  "operator_id":"operator_2",
  "password":"op2"
}
</code>
   
