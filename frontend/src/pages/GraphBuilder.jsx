import React, { useState } from 'react';

const GraphBuilder = () => {
  const [graphData, setGraphData] = useState({ nodes: [], edges: [] });
  
  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        try {
          const data = JSON.parse(e.target.result);
          setGraphData(data);
        } catch (err) {
          console.error('Error parsing file:', err);
        }
      };
      reader.readAsText(file);
    }
  };

  return (
    <div>
      <h1>Supply Chain Graph Builder</h1>
      <input type="file" accept=".json,.csv" onChange={handleFileUpload} />
      <div id="graph-container"></div>
    </div>
  );
};

export default GraphBuilder;
