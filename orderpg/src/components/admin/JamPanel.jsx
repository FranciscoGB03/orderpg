import { useState, useEffect } from "react";
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const JamPanel = () => {
  const [jam, setJam] = useState({
    name: "",
    active: false,
  });
  const [jams, setJams] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetchJams();
  }, []);

  const fetchJams = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/allJams`);
      setJams(response.data);
    } catch (error) {
      console.error("Error al obtener mermeladas:", error);
    }
  };

  const handleChange = (e) => {
    setJam({ ...jam, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("");

    try {
      if (editingId) {
        await axios.put(`${API_BASE_URL}/update-jam/${editingId}`, jam);
        setMessage("Registro actualizado con éxito.");
      } else {
        await axios.post(`${API_BASE_URL}/add-jam`, jam);
        setMessage("Registro agregado con éxito.");
      }

      setJam({ name: "", active: false });
      setEditingId(null);
      fetchJams();
    } catch (error) {
      console.error(error);
      setMessage("Hubo un error al guardar el registro.");
    }
  };

  const handleEdit = (syrup) => {
    setJam(syrup);
    setEditingId(syrup.id);
  };

  return (
    <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-lg">
      <h1 className="text-2xl font-bold text-center text-gray-800 mb-4">
        {editingId ? "Editar Mermelada" : "Agregar Nueva Mermelada"}
      </h1>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block text-gray-700">Nombre de la mermelada:</label>
          <input
            type="text"
            name="name"
            value={jam.name}
            onChange={handleChange}
            required
            className="w-full px-3 py-2 border rounded-lg focus:ring focus:ring-blue-300"
          />
        </div>
        <div className="flex items-center space-x-2">
          <label className="text-gray-700">Existencia:</label>
          <input
            type="checkbox"
            name="active"
            checked={jam.active}
            onChange={() => setJam({ ...jam, active: !jam.active })}
            className="w-5 h-5"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition"
        >
          {editingId ? "Actualizar Jarabe" : "Agregar mermelada"}
        </button>
      </form>
      {message && (
        <p className="mt-4 text-green-600 text-center font-semibold">
          {message}
        </p>
      )}

      <h2 className="text-xl font-bold text-gray-800 mt-6">
        Mermeladas Disponibles
      </h2>
      <ul className="space-y-3 mt-2">
        {jams.map((r) => (
          <li
            key={r.id}
            className={`border p-4 rounded-lg flex justify-between items-center ${
              r.active ? "bg-green-300" : "bg-red-300 text-white"
            }`}
          >
            <div>
              <h3 className="font-semibold">{r.name}</h3>
            </div>
            <button
              onClick={() => handleEdit(r)}
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
export default JamPanel;
