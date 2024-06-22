import React from 'react';
import InventoryList from './components/InventoryList';
import AddProduct from './components/AddProduct';

function App() {
    return (
        <div>
            <h1>Inventario IA</h1>
            <AddProduct />
            <InventoryList />
        </div>
    );
}

export default App;
