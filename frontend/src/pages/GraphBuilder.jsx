import React, { useState } from 'react';
import { Upload, Button, message } from 'antd';
import axios from 'axios';

const GraphBuilder = () => {
  const [fileList, setFileList] = useState([]);

  const handleUpload = async (info) => {
    const file = info.file;
    if (file.type === 'application/json' || file.type === 'text/csv') {
      const formData = new FormData();
      formData.append('file', file);
      
      try {
        const response = await axios.post('/api/supply-chain/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        });
        message.success('Upload successful');
      } catch (error) {
        message.error('Upload failed');
      }
    }
  };

  return (
    <div>
      <h2>Supply Chain Graph Builder</h2>
      <Upload
        beforeUpload={() => false}
        onChange={handleUpload}
        fileList={fileList}
      >
        <Button icon={<UploadOutlined />}>Click to Upload</Button>
      </Upload>
    </div>
  );
};

export default GraphBuilder;
