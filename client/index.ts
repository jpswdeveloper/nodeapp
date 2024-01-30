import express from "express"
import cors from "cors"

const app = express()

app.use(cors())
app.get("/", (req, res) => {
  // This Home
  res.send({ message: "Welcome to Express" })
})

// Listen the server
const port = process.env.PORT || 4000 // server will run on 4000 or on env

app.listen(port, () => {
  console.log(`Server is running on port ${port}`)
})
