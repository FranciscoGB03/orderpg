import { useState } from "react";
import MenuPanel from "./MenuPanel";
import SyrupPanel from "./SyrupPanel";
import JamPanel from "./JamPanel";
import ToppingPanel from "./ToppingPanel";

const AdminPanel = () => {
  const [activeTab, setActiveTab] = useState("menu");

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-6">
      <div className="bg-white shadow-lg rounded-lg p-4 w-full max-w-2xl mb-6">
        <nav className="flex justify-around border-b pb-2">
          {["menu", "jarabes", "mermeladas", "toppings"].map((tab) => (
            <button
              key={tab}
              className={`px-4 py-2 ${
                activeTab === tab
                  ? "text-blue-600 font-bold border-b-2 border-blue-600"
                  : "text-gray-500"
              }`}
              onClick={() => setActiveTab(tab)}
            >
              {tab.toUpperCase()}
            </button>
          ))}
        </nav>
      </div>

      {activeTab === "menu" && <MenuPanel />}
      {activeTab === "jarabes" && <SyrupPanel />}
      {activeTab === "mermeladas" && <JamPanel />}
      {activeTab === "toppings" && <ToppingPanel />}
    </div>
  );
};

export default AdminPanel;
