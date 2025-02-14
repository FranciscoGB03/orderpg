import { useState, useEffect } from "react";
import axios from "axios";
import MarkdownEditor from "../../utils/MarkDownEditor";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const MenuPanel = () => {
  const [menu, setMenu] = useState({
    name: "",
    price: "",
    description: "",
    active: false,
  });
  const [menus, setMenus] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchMenus();
  }, []);

  const fetchMenus = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/allMenus`);
      setMenus(response.data);
    } catch (error) {
      console.error("Error al obtener menús:", error);
    }
  };

  const handleChange = (e) => {
    setMenu({ ...menu, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      if (editingId) {
        await axios.put(`${API_BASE_URL}/update-menu/${editingId}`, menu);
        setMessage("Menú actualizado con éxito.");
      } else {
        await axios.post(`${API_BASE_URL}/add-menu`, menu);
        setMessage("Menú agregado con éxito.");
      }

      setMenu({ name: "", price: "", description: "", active: false });
      setEditingId(null);
      fetchMenus();
    } catch (error) {
      console.error(error);
      setMessage("Hubo un error al guardar el menú.");
    }
  };

  const handleEdit = (menu) => {
    setMenu(menu);
    setEditingId(menu.id);
  };

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-lg">
      <h1 className="text-2xl font-bold text-center text-gray-800 mb-4">
        {editingId ? "Editar Menú" : "Agregar Nuevo Menú"}
      </h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-gray-700">Nombre del Postre:</label>
          <input
            type="text"
            name="name"
            value={menu.name}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300"
          />
        </div>
        <div>
          <label className="block text-gray-700">Precio:</label>
          <input
            type="number"
            name="price"
            value={menu.price}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300"
          />
        </div>
        <div>
          <label className="block text-gray-700">Descripción:</label>
          <MarkdownEditor
            value={menu.description}
            onChange={(e) => setMenu({ ...menu, description: e.text })}
          />
        </div>
        <div className="flex items-center space-x-2">
          <label className="text-gray-700">Existencia:</label>
          <input
            type="checkbox"
            name="active"
            checked={menu.active}
            onChange={() => setMenu({ ...menu, active: !menu.active })}
            className="w-5 h-5"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
        >
          {editingId ? "Actualizar Menú" : "Agregar Menú"}
        </button>
      </form>
      {message && (
        <p className="mt-4 text-green-600 text-center font-semibold">
          {message}
        </p>
      )}

      <h2 className="text-xl font-bold text-gray-800 mt-6">
        Menús Disponibles
      </h2>
      <ul className="space-y-3 mt-2">
        {menus.map((m) => (
          <li
            key={m.id}
            className={`border p-4 rounded-lg flex justify-between items-center ${
              m.active ? "bg-green-300" : "bg-red-300 text-white"
            }`}
          >
            <div>
              <h3 className="font-semibold">
                {m.name} - ${m.price}
              </h3>
              <p className="text-gray-600">{m.description}</p>
            </div>
            <button
              onClick={() => handleEdit(m)}
              className="bg-yellow-500 text-white px-3 py-1 rounded-lg hover:bg-yellow-600"
            >
              Editar
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MenuPanel;
