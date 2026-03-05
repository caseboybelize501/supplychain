import React, { useEffect, useState } from 'react';
import axios from 'axios';

const RiskReport = () => {
  const [reportData, setReportData] = useState(null);

  useEffect(() => {
    // Fetch report data
    axios.get('/api/simulation/123/report').then(response => {
      setReportData(response.data);
    });
  }, []);

  return (
    <div>
      <h2>Risk Report</h2>
      {reportData && (
        <div>
          <p>Executive Summary: {reportData.narrative.executive_summary}</p>
          <h3>Key Findings:</h3>
          <ul>
            {reportData.narrative.key_findings.map((finding, i) => (
              <li key={i}>{finding}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default RiskReport;
