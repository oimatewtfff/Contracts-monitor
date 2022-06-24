import React from 'react';
import Table from 'react-bootstrap/Table'

const TTable = (props) => {
    return (
        <Table table position-relative variant="primary" className="mt-5">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>№ Контракта</th>
                    <th>Стоимость, USD</th>
                    <th>Стоимость, Руб.</th>
                    <th>Срок поставки</th>
                </tr>
            </thead>
            <tbody>
                {props.contracts.map(contracts => (
                    <tr key={contracts.id}>
                        <td>{contracts.id}</td>
                        <td>{contracts.contract}</td>
                        <td>{contracts.price_usd}</td>
                        <td>{contracts.price_rub}</td>
                        <td>{contracts.date}</td>
                    </tr>
                ))}
            </tbody>
        </Table>
    );
};

export default TTable;