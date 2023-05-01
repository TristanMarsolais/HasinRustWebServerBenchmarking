const express = require('express');
const app = express();
const path = require('path');

const PORT = process.env.PORT || 8084;

// Set the public directory as a static folder
app.use(express.static(path.join(__dirname, 'public')));

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
