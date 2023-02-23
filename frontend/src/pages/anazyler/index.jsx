import {
    Box,
    Button,
    FormControlLabel,
    Radio,
    RadioGroup,
    Typography,
    useTheme
} from "@mui/material";
import { tokens } from "../../theme";
import LineChart from "../../components/LineChart";
import BarChart from "../../components/BarChart";
import StatBox from "../../components/StatBox";
import ProgressCircle from "../../components/ProgressCircle";
import Header from "../../components/Header";
import TextField from '@mui/material/TextField';
import React, { useState } from 'react';
import axios from "axios";

const Dashboard = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [result, setResult] = useState(0);
    const [input, setInput] = useState('text');

    const [resultsArray, setResultsArray] = useState(['0', '1', '0', '0', '0', '1', '0', '0', '0']);

    const [message, setMessage] = useState('');

    const handleChange = event => {
        setMessage(event.target.value);

        console.log('value is:', event.target.value);
    };

/*    export default function Results() {
        const [resultsArray, setResultsArray] = useState(['0', '0', '0'])
        const fetchResultsArray = async () => {
            const response = await fetch("http://localhost:8000/")
            const results = await response.json()
            setResultsArray(results.data)
        }
    }*//*

    const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: JSON.stringify({data: message}),
    };*/

    function getResults() {
        axios.post(`http://127.0.0.1:8080/analyse/news`, {message})
            .then(res => {
                const results = res.data.d;
                setResultsArray(results);
            })
        /*axios.get(`http://127.0.0.1:8080/results`)
            .then(res => {
                const results = res.data.d;
                setResultsArray( results );
            })*/
        /*        axios({
                    method: 'post',
                    url: '/results/',
                    data: "formData",
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                })
                    .then(response => {
                        const results = response.data.d;
                        setResultsArray( results );
                        console.log(results);
                    })
                    .catch(error => {
                        console.error(error);
                    });*/
    }

    /*const [value, setValue] = useState('text');

    const handleChange = (event) => {
        setValue(event.target.value);
    };*/

/*    function change(){
        console.table(resultsArray);
        setResultsArray([randomNumberInRange(0,1), randomNumberInRange(0,1),randomNumberInRange(0,1)])
        console.table(resultsArray);
    }*/

    return (
        <Box m="20px">
            {/* HEADER */}
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header title="Analyzer Dashboard" subtitle="Text analysis dashboard" />
            </Box>
            <Box display="grid"
                 gridTemplateColumns="repeat(12, 1fr)"
                 gridAutoRows="200px"
                 gap="10px"
            >
                {/*ROW 1*/}
                <Box
                    gridRow="span 2"
                    gridColumn="span 12"
                    backgroundColor={colors.primary[400]}
                    p="30px"
                >
                    <Typography variant="h5" fontWeight="600">
                        Information Input
                    </Typography>
                    <Box display="flex" justifyContent="start">
                        <RadioGroup
                            row
                            defaultValue="text"
                            /*value={value}
                            onChange={handleChange}*/
                        >
                            <FormControlLabel  value="text" control={<Radio color="secondary" onClick={() => setInput('text')} />} label="Text Input" />
                            <FormControlLabel value="file" control={<Radio color="secondary" onClick={() => setInput('file')} />} label="File Input" />
                        </RadioGroup>
                    </Box>
                    <Box
                        display="flex"
                        flexDirection="column"
                        alignItems="center"
                        mt="5px"
                    >
                        <TextField
                            fullWidth
                            fullHeight
                            placeholder='Data input'
                            required={true}
                            multiline={true}
                            rows='10'
                            onChange={handleChange}
                            value={message}
                        />
                    </Box>
                    <Box display="flex" justifyContent="end" mt="20px">
                        <Button type="submit" color="secondary" variant="contained" onClick={getResults}>
                            Submit
                        </Button>
                    </Box>
                </Box>
                {/*ROW 2*/}
                {resultsArray.map((Item, index) => (
                        <Box
                            className={"column"} key={index}
                            gridColumn="span 4"
                            backgroundColor={colors.primary[400]}
                            p="10px"
                        >
                            <Typography variant="h5" fontWeight="600">
                                Model {index + 1}
                            </Typography>
                            <Box
                                display="flex"
                                flexDirection="column"
                                alignItems="center"
                                mt="5px"
                            >
                                <ProgressCircle progress={Item} size="125" />
                                <Typography
                                    variant="h5"
                                    color={Item === '1'?colors.redAccent[500]:colors.greenAccent[500]}/*{getColor(resultsArray[0])}*/
                                    sx={{ mt: "15px" }}
                                >
                                    Based on this model, the information provided is probably {Item === '1'?'FALSE':'TRUE'}
                                </Typography>
                            </Box>
                        </Box>
                ))}

            </Box>

        </Box>
    );
};

export default Dashboard;