import { useState } from "react";
import { Routes, Route } from "react-router-dom";

import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";

import Sidebar from "./pages/global/SideBar";
import Analyzer from "./pages/anazyler";
import Description from "./pages/description";
import AboutUs from "./pages/aboutUs";

function App() {
    const [theme, colorMode] = useMode();
    const [isSidebar, setIsSidebar] = useState(true);

    return (
        <ColorModeContext.Provider value={colorMode}>
            <ThemeProvider theme={theme}>
                <CssBaseline />
                <div className="app">
                    <Sidebar isSidebar={isSidebar} />
                    <main className="content">
                        <Routes>
                            <Route path="/" element={<Analyzer />} />
                            <Route path="/description" element={<Description />} />
                            <Route path="/aboutUs" element={<AboutUs />} />
                        </Routes>
                    </main>
                </div>
            </ThemeProvider>
        </ColorModeContext.Provider>
    );
}

export default App;
