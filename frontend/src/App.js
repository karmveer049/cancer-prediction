import { useState } from "react";
import axios from "axios";

function App() {
    const [features, setFeatures] = useState(new Array(30).fill(0));
    const [prediction, setPrediction] = useState(null);

    const handleChange = (index, value) => {
        const newFeatures = [...features];
        newFeatures[index] = parseFloat(value) || 0;
        setFeatures(newFeatures);
    };

    const handleSubmit = async () => {
        try {
            const response = await axios.post("/predict", { features });
            setPrediction(response.data.prediction);
        } catch (error) {
            console.error("Error:", error);
        }
    };

    return (
        <div>
            <h1>Cancer Prediction</h1>
            {features.map((_, index) => (
                <input
                    key={index}
                    type="number"
                    placeholder={`Feature ${index + 1}`}
                    onChange={(e) => handleChange(index, e.target.value)}
                />
            ))}
            <button onClick={handleSubmit}>Predict</button>
            {prediction !== null && <h2>Prediction: {prediction}</h2>}
        </div>
    );
}

export default App;
