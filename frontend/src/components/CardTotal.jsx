import React from 'react';
import Card from 'react-bootstrap/Card'

const CardTotal = (props) => {
    return (<>
        <Card className="mt-5" border="dark" style={{ width: '18rem' }}>
            <Card.Header>Total, USD</Card.Header>
            <Card.Body>
                <Card.Title>{props.total}</Card.Title>
            </Card.Body>
        </Card>
        <br />
    </>
    );
};

export default CardTotal;