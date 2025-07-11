import axios from 'axios';
import { useEffect, useState } from 'react';

export default function Product()
{
    const [products,setProducts]=useState([])
    const fetchProducts=()=>{
        axios
        .get("https://djangoreact25.pythonanywhere.com/allproducts/")
        .then((response)=>setProducts(response.data))
        .catch((error)=>console.error(error))
    }

    useEffect(()=>{
        fetchProducts();
    },[])

    return(
        <div>
        <h1>All Products</h1>
        <div>
            {products.map((p)=>(
                <div key={p.id}>
                        <img src={p.photo} alt={p.name} style={{height:200,width:200}}/>
                        <h2>{p.name}</h2>
                        <p>{p.category}</p>
                        <p>Price:-{p.price}</p>
                </div>
            ))}
        </div>
        </div>
    )
}