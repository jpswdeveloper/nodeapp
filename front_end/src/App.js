import logo from './logo.svg';
import './App.css';
import {useState, useEffect} from 'react';

function App () {
  const [message, setMessage] = useState ('');

  const fetchData = async () => {
    try {
      const response = await fetch ('http://localhost:4000');
      console.log (response);
      if (!response.ok) {
        throw new Error ('Failed to fetch data');
      }

      const data = await response.json ();
      console.log ({data});
      setMessage (data.message);
    } catch (error) {
      console.error ('Error fetching data:', error.message);
    }
  };

  useEffect (() => {
    fetchData ();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <p>This is test one {message}</p>
        <p />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

      </header>
    </div>
  );
}

export default App;
