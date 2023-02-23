import { useState } from "react";
import { ProSidebar, Menu, MenuItem } from 'react-pro-sidebar';
import 'react-pro-sidebar/dist/css/styles.css';
import { Box, IconButton, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import TroubleshootOutlinedIcon from '@mui/icons-material/TroubleshootOutlined';
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import PeopleOutlineOutlinedIcon from '@mui/icons-material/PeopleOutlineOutlined';
import ListOutlinedIcon from '@mui/icons-material/ListOutlined';

const Item = ({ title, to, icon, selected, setSelected }) => {
    return (
        <MenuItem
            active={selected === title}
            onClick={() => setSelected(title)}
            icon={icon}
        >
            <Typography>{title}</Typography>
            <Link to={to} />
        </MenuItem>
    );
};

const Sidebar = () => {
    const [isCollapsed, setIsCollapsed] = useState(false);
    const [selected, setSelected] = useState("Analyzer");

    return (
        <Box
            sx={{
                "& .pro-icon-wrapper": {
                    backgroundColor: "transparent !important"
                },
            "$ .pro-inner-item":{
                    padding: "5px 35px 5px 20px !important"
            },
            "$ .pro-inner-item:hover":{
                padding: "#868dfb !important"
            },
            "$ .pro-menu-item.active":{
                padding: "#6870fa !important"
            }
        }}
        >
            <ProSidebar collapsed={isCollapsed}>
                <Menu iconShape="square">
                    <MenuItem
                        onClick={() => setIsCollapsed(!isCollapsed)}
                        icon={isCollapsed ? <ListOutlinedIcon /> : undefined}
                        style={{
                            margin: "10px 0 20px 0",
                        }}
                    >
                        {!isCollapsed && (
                            <Box
                                display="flex"
                                justifyContent="space-between"
                                alignItems="center"
                                ml="15px"
                            >
                                <IconButton onClick={() => setIsCollapsed(!isCollapsed)}>
                                    <ListOutlinedIcon />
                                </IconButton>
                                <Typography variant="h3" >
                                    DISInfo Analyzer
                                </Typography>

                            </Box>
                        )}
                    </MenuItem>

                    {!isCollapsed && (
                        <Box mb="25px">
                            <Box display="flex" justifyContent="center" alignItems="center">
                                <img
                                    //alt="profile-user"
                                    alt="team-profile"
                                    width="100"
                                    height="100"
                                    src={`.//../resources/logo.png`}
                                    style={{ cursor: "pointer", borderRadius: "50%" }}
                                />
                            </Box>
                            <Box textAlign="center">
                                <Typography
                                    variant="h2"
                                    fontWeight="bold"
                                    sx={{ m: "10px 0 0 0" }}
                                >
                                    NCS
                                </Typography>
                                <Typography variant="h5" >
                                    Night Coding Sergeants
                                </Typography>
                            </Box>
                        </Box>
                    )}

                    <Box paddingLeft={isCollapsed ? undefined : "10%"}>
                        <Item
                            title="Analyzer"
                            to="/"
                            icon={<TroubleshootOutlinedIcon />}
                            selected={selected}
                            setSelected={setSelected}
                        />

                        <Typography
                            variant="h6"
                            sx={{ m: "15px 0 5px 20px" }}
                        >
                            Info
                        </Typography>
                        <Item
                            title="Description"
                            to="/description"
                            icon={<HelpOutlineOutlinedIcon />}
                            selected={selected}
                            setSelected={setSelected}
                        />
                        <Item
                        title="About Us"
                        to="/aboutUs"
                        icon={<PeopleOutlineOutlinedIcon />}
                        selected={selected}
                        setSelected={setSelected}
                    />
                    </Box>
                </Menu>
            </ProSidebar>

        </Box>
    );
};

export default Sidebar;