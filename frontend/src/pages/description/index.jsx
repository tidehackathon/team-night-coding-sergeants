import { Box, useTheme } from "@mui/material";
import Header from "../../components/Header";
import Accordion from "@mui/material/Accordion";
import AccordionSummary from "@mui/material/AccordionSummary";
import AccordionDetails from "@mui/material/AccordionDetails";
import Typography from "@mui/material/Typography";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import { tokens } from "../../theme";

const Description = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return (
        <Box m="20px">
            <Header title="Description" subtitle="Answers to the most important questions" />

            <Accordion defaultExpanded>
                <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                    <Typography color={colors.greenAccent[500]} variant="h5">
                        Question
                    </Typography>
                </AccordionSummary>
                <AccordionDetails>
                    <Typography>
                        Text
                    </Typography>
                </AccordionDetails>
            </Accordion><Accordion defaultExpanded>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography color={colors.greenAccent[500]} variant="h5">
                    Question
                </Typography>
            </AccordionSummary>
            <AccordionDetails>
                <Typography>
                    Text
                </Typography>
            </AccordionDetails>
        </Accordion><Accordion defaultExpanded>
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography color={colors.greenAccent[500]} variant="h5">
                    Question
                </Typography>
            </AccordionSummary>
            <AccordionDetails>
                <Typography>
                    Text
                </Typography>
            </AccordionDetails>
        </Accordion>
        </Box>
    );
};

export default Description;