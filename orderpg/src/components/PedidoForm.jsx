import axios from "axios";
import { useState, useEffect } from "react";
import MarkdownEditor from "../utils/MarkDownEditor";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const PedidoForm = () => {
  const [form, setForm] = useState({
    customer_name: "",
    products: [], // Ahora es un array
    phone: "",
    address: "",
  });

  const [message, setMessage] = useState("");
  const [menus, setMenus] = useState([]);

  useEffect(() => {
    axios
      .get(`${API_BASE_URL}/menus`)
      .then((response) => setMenus(response.data))
      .catch((error) => console.error("Error al obtener menús:", error));
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleProductSelect = (e) => {
    const selectedId = parseInt(e.target.value);
    if (!selectedId) return;

    const selectedProduct = menus.find((menu) => menu.id === selectedId);
    if (!selectedProduct) return;

    // Evitar duplicados
    if (form.products.some((p) => p.id === selectedProduct.id)) return;

    setForm({
      ...form,
      products: [
        ...form.products,
        { ...selectedProduct, amount: 1, notes: "" }, // Se inicializa con cantidad 1 y notes vacío
      ],
    });
  };

  const handleProductChange = (index, field, value) => {
    const updatedProducts = [...form.products];
    updatedProducts[index][field] = value;
    setForm({ ...form, products: updatedProducts });
  };

  const handleRemoveProduct = (index) => {
    const updatedProducts = form.products.filter((_, i) => i !== index);
    setForm({ ...form, products: updatedProducts });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(""); // Limpiar mensaje previo

    try {
      const response = await axios.post(`${API_BASE_URL}/order`, form);
      if (response.status === 200) {
        setMessage("Pedido enviado con éxito. 🚀");
        setForm({
          customer_name: "",
          products: [],
          phone: "",
          address: "",
        }); // Limpiar formulario
      }
    } catch (error) {
      console.error(error);
      setMessage("Hubo un error al enviar el pedido.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-md">
        <h1 className="text-2xl font-bold text-center text-gray-800 mb-4">
          Realizar Pedido
        </h1>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-gray-700">Nombre del Cliente:</label>
            <input
              type="text"
              name="customer_name"
              value={form.customer_name}
              onChange={handleChange}
              required
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
            />
          </div>

          <div>
            <label className="block text-gray-700">
              Selecciona el/los producto(s):
            </label>
            <select
              id="product"
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
              onChange={handleProductSelect}
            >
              <option value="">--Elige una opción--</option>
              {menus.map((menu) => (
                <option key={menu.id} value={menu.id}>
                  {menu.name}
                </option>
              ))}
            </select>
          </div>

          {/* Lista de productos seleccionados */}
          {form.products.length > 0 && (
            <div className="space-y-4">
              {form.products.map((product, index) => (
                <div
                  key={product.id}
                  className="border p-4 rounded-lg bg-gray-50"
                >
                  <div className="flex justify-between">
                    <h3 className="text-lg font-semibold">{product.name}</h3>
                    <button
                      type="button"
                      onClick={() => handleRemoveProduct(index)}
                      className="text-red-500 hover:text-red-700"
                    >
                      ✖
                    </button>
                  </div>
                  <p className="text-gray-600">
                    Precio por pieza: ${product.price}
                  </p>
                  <MarkdownEditor
                    value={product.description}
                    showMenu={false}
                    showMd={false}
                    autoHeight={true}
                  />
                  <div>
                    <label className="block text-gray-700">Cantidad:</label>
                    <input
                      type="number"
                      min="1"
                      name="amount"
                      value={product.amount}
                      onChange={(e) =>
                        handleProductChange(
                          index,
                          "amount",
                          parseInt(e.target.value) || 1
                        )
                      }
                      className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                  </div>
                  <div>
                    <label className="block text-gray-700">
                      Algún comentario:
                    </label>
                    <input
                      type="text"
                      name="notes"
                      value={product.notes}
                      onChange={(e) =>
                        handleProductChange(index, "notes", e.target.value)
                      }
                      className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
                    />
                  </div>
                  <p className="font-semibold">
                    Total: ${product.amount * product.price}
                  </p>
                </div>
              ))}
            </div>
          )}

          {/* Total General */}
          {form.products.length > 0 && (
            <p className="text-lg font-bold">
              Total General: $
              {form.products.reduce(
                (sum, prod) => sum + prod.amount * prod.price,
                0
              )}
            </p>
          )}

          <div>
            <label className="block text-gray-700">Número de contacto:</label>
            <input
              type="text"
              name="phone"
              maxLength={10}
              value={form.phone}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
            />
          </div>

          <div>
            <label className="block text-gray-700">
              Dirección a enviar (opcional):
            </label>
            <input
              type="text"
              name="address"
              value={form.address}
              onChange={handleChange}
              className="w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring focus:ring-blue-300"
            />
          </div>

          <button
            type="submit"
            className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
          >
            Enviar Pedido
          </button>
        </form>

        {message && (
          <p className="mt-4 text-green-600 text-center font-semibold">
            {message}
          </p>
        )}
      </div>
    </div>
  );
};

export default PedidoForm;
