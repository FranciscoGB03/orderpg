import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import PedidoForm from "./components/PedidoForm";
import AdminPanel from "./components/admin/AdminPanel";
import "./app.css";
import "react-markdown-editor-lite/lib/index.css";

const App = () => {
  return (
    <Router basename="/test">
      <nav className="bg-blue-600 text-white p-4 flex justify-center space-x-4">
        <Link to="/" className="hover:underline">
          Pedidos
        </Link>
      </nav>
      <Routes>
        <Route path="/" element={<PedidoForm />} />
        <Route path="/admin" element={<AdminPanel />} />
      </Routes>
    </Router>
  );
};

export default App;
