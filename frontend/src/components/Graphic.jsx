import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';


const Graphic = (props) => {
  return (
    <ResponsiveContainer width="90%" height="35%">
      <LineChart
        width={400}
        height={300}
        data={props.contracts.map(contracts => ({
          Date: contracts.date,
          Price: contracts.price_usd
        }))}
        margin={{
          top: 150,
          right: 5,
          left: 5,
          bottom: 5,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="Date" />
        <YAxis dataKey="Price" />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="Price" stroke="#8884d8" activeDot={{ r: 8 }} />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default Graphic;