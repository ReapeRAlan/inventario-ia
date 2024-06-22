import React, { useState } from 'react';
import axios from 'axios';

function AddProduct() {
    const [form, setForm] = useState({
        nombre_producto: '',
        cantidad: '',
        precio: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setForm({ ...form, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/inventario', form)
            .then(response => {
                console.log('Product added:', response.data);
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="nombre_producto"
                placeholder="Nombre del producto"
                value={form.nombre_producto}
                onChange={handleChange}
            />
            <input
                type="number"
                name="cantidad"
                placeholder="Cantidad"
                value={form.cantidad}
                onChange={handleChange}
            />
            <input
                type="number"
                step="0.01"
                name="precio"
                placeholder="Precio"
                value={form.precio}
                onChange={handleChange}
            />
            <button type="submit">Añadir Producto</button>
        </form>
    );
}

export default AddProduct;
