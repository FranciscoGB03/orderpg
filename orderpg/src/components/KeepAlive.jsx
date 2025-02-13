import { useEffect } from "react";

const KeepAlive = () => {
  useEffect(() => {
    const pingServer = async () => {
      try {
        await fetch("https://orderpg.onrender.com/ping", { method: "GET" });
        console.log("Ping enviado al servidor");
      } catch (error) {
        console.error("Error al hacer ping al servidor:", error);
      }
    };

    pingServer(); // Llamado inicial inmediato

    const interval = setInterval(pingServer, 120 * 1000); // Cada 2 minutos

    return () => clearInterval(interval);
  }, []);

  return null;
};

export default KeepAlive;
