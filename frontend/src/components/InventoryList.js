import React, { useEffect, useState } from 'react';
import axios from 'axios';

function InventoryList() {
    const [inventory, setInventory] = useState([]);

    useEffect(() => {
        axios.get('/inventario')
            .then(response => setInventory(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <ul>
            {inventory.map(item => (
                <li key={item.id}>
                    {item.nombre_producto} - {item.cantidad} unidades - ${item.precio}
                </li>
            ))}
        </ul>
    );
}

export default InventoryList;
