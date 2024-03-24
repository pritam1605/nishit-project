import React, {useState, useEffect} from 'react';
import './App.css';

import Home from './pages/Home';

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://127.0.0.1:5000/", {
      'methods':'POST',
      headers: {
        'Content-Type':'application/json'
      }
    }).then(
      resp => resp.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    ).catch(error => console.log(error))
  }, [])

  return (
    <div className="App">
      <Home />
    </div>
  );
}

export default App;
