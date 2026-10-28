try { require("dotenv").config(); } catch (e) {}
const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => res.sendFile(path.join(__dirname, "index.html")));

app.get("/health", (req, res) =>
  res.json({ status: "ok", project: "Team M: IoT Sensor Analytics", stack: "node" })
);

app.post("/api/ingest", (req, res) => {
  // TODO: Body: {device, value, ts}
  res.status(501).json({ error: "Not implemented", todo: "Body: {device, value, ts}" });
});

app.get("/api/series", (req, res) => {
  // TODO: Aggregated series by interval
  res.status(501).json({ error: "Not implemented", todo: "Aggregated series by interval" });
});

app.get("/api/stream", (req, res) => {
  // TODO: SSE live feed
  res.status(501).json({ error: "Not implemented", todo: "SSE live feed" });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Team M server running on http://localhost:${PORT}`));
