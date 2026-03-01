import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard API endpoint:', endpoint);
        console.log('Fetched data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {data.map((item, idx) => (
          <li key={item.id || idx}>{item.name || JSON.stringify(item)}</li>
        ))}
      </ul>
    </div>
  );
};
export default Leaderboard;
