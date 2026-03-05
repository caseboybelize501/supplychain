import React, { useState } from 'react';
import { Button, Select, InputNumber } from 'antd';
import axios from 'axios';

const ScenarioRunner = () => {
  const [chainId, setChainId] = useState('');
  const [scenario, setScenario] = useState('');
  const [iterations, setIterations] = useState(1000);

  const runSimulation = async () => {
    try {
      const response = await axios.post('/api/simulation/run', {
        chain_id: chainId,
        scenario,
        iterations
      });
      alert(`Simulation started with job ID: ${response.data.job_id}`);
    } catch (error) {
      alert('Failed to start simulation');
    }
  };

  return (
    <div>
      <h2>Scenario Runner</h2>
      <Input placeholder="Chain ID" value={chainId} onChange={(e) => setChainId(e.target.value)} />
      <Select style={{ width: '100%' }} value={scenario} onChange={setScenario}>
        <Select.Option value="port_strike">Port Strike</Select.Option>
        <Select.Option value="supplier_bankruptcy">Supplier Bankruptcy</Select.Option>
        {/* Add more scenarios */}
      </Select>
      <InputNumber min={100} max={10000} value={iterations} onChange={setIterations} />
      <Button type="primary" onClick={runSimulation}>Run Simulation</Button>
    </div>
  );
};

export default ScenarioRunner;
