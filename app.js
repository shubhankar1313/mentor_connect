const express = require('express');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const PORT = 3000;

// Serve static files (like your HTML page)
app.use(express.static(path.join(__dirname, 'public')));

// API route to get mentor recommendations
app.get('/get-mentors', (req, res) => {
    const keywords = req.query.keywords || 'IT'; // Default keyword if none provided

    // Spawn a new Python process
    const pythonProcess = spawn('python3', [path.join(__dirname, 'scripts', 'Recommendation.py'), keywords]);

    let dataToSend = '';

    // Collect data from the Python script
    pythonProcess.stdout.on('data', (data) => {
        dataToSend += data.toString();
    });

    pythonProcess.on('close', (code) => {
        // Convert the string data to JSON
        const mentorData = JSON.parse(dataToSend);
        res.json(mentorData);
    });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
