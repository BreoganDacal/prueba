import React, { useEffect, useState } from 'react';

function App() {
  const [time, setTime] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(process.env.REACT_APP_BACKEND_URL + '/api/data')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => setTime(data.time))
      .catch((error) => setError(error.message));
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>Neon + Vercel Example</h1>
      {error && <p style={{ color: 'red' }}>Error: {error}</p>}
      {time ? (
        <p>Current time from backend: {new Date(time).toLocaleString()}</p>
      ) : (
        <p>Loading time from backend...</p>
      )}
    </div>
  );
}

export default App;
