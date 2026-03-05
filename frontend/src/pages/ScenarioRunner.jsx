import React, { useState } from 'react';

const ScenarioRunner = () => {
  const [chainId, setChainId] = useState('');
  const [scenario, setScenario] = useState('port_strike');
  const [iterations, setIterations] = useState(1000);
  
  const handleRunSimulation = async () => {
    try {
      const response = await fetch('/api/simulation/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ chain_id: chainId, scenario, iterations })
      });
      
      const result = await response.json();
      console.log('Simulation started:', result);
    } catch (error) {
      console.error('Error starting simulation:', error);
    }
  };

  return (
    <div>
      <h1>Scenario Runner</h1>
      <input placeholder="Chain ID" value={chainId} onChange={(e) => setChainId(e.target.value)} />
      <select value={scenario} onChange={(e) => setScenario(e.target.value)}>
        <option value="port_strike">Port Strike</option>
        <option value="supplier_bankruptcy">Supplier Bankruptcy</option>
        <option value="earthquake_region">Earthquake in Region</option>
        <option value="demand_spike_3x">Demand Spike 3x</option>
        <option value="tariff_increase_25pct">Tariff Increase 25%</option>
      </select>
      <input type="number" value={iterations} onChange={(e) => setIterations(parseInt(e.target.value))} />
      <button onClick={handleRunSimulation}>Run Simulation</button>
    </div>
  );
};

export default ScenarioRunner;
