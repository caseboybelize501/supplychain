import React, { useEffect, useState } from 'react';

const RiskReport = () => {
  const [reportData, setReportData] = useState(null);
  
  useEffect(() => {
    // Mock data for demonstration
    setReportData({
      executive_summary: "Supply chain risk assessment shows significant exposure to port strikes and supplier failures.",
      key_findings: ["High revenue at risk during port strikes", "Supplier bankruptcy impacts recovery time"],
      mitigations: [
        { action: "Diversify suppliers", cost_estimate: "$50K", risk_reduction_pct: 40, roi_rank: 1 },
        { action: "Implement buffer stock", cost_estimate: "$20K", risk_reduction_pct: 30, roi_rank: 2 }
      ],
      immediate_actions: ["Review supplier contracts", "Establish backup suppliers"],
      monitoring_kpis: ["Recovery time", "Revenue at risk"]
    });
  }, []);

  return (
    <div>
      <h1>Risk Report</h1>
      {reportData && (
        <div>
          <p>{reportData.executive_summary}</p>
          <h2>Key Findings</h2>
          <ul>
            {reportData.key_findings.map((finding, i) => (<li key={i}>{finding}</li>))}
          </ul>
          <h2>Mitigations</h2>
          <table>
            <thead>
              <tr><th>Action</th><th>Cost</th><th>Risk Reduction</th><th>ROI Rank</th></tr>
            </thead>
            <tbody>
              {reportData.mitigations.map((m, i) => (
                <tr key={i}>
                  <td>{m.action}</td>
                  <td>{m.cost_estimate}</td>
                  <td>{m.risk_reduction_pct}%</td>
                  <td>{m.roi_rank}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default RiskReport;
