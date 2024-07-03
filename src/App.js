import { BrowserRouter, Route, Routes } from "react-router-dom";

import CourseDashboard from "./pages/CourseDashboard";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<CourseDashboard />} />
      </Routes>
    </BrowserRouter>
  )
}
