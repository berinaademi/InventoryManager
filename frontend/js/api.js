const API_URL = "https://inventorymanager-u6v6.onrender.com/api";

async function testConnection() {
    try {
        const response = await fetch(`${API_URL}/items/shopping-list`);
        const data = await response.json();
        console.log("Backend Connection Successful!", data);
        alert("Success! Check the console for the shopping list.");
    } catch (error) {
        console.error("Connection failed:", error);
        alert("Backend is not reaching the frontend. Check CORS or if Flask is running.");
    }
}