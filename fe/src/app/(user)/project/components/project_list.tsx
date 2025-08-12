'use client';

import projectApi from "@/app/services/api/projectApi";
import withAuth from "@/hook/check_auth";
import { Project } from "@/types/project";
import { Box, Card, CardContent, CardMedia, Fade, Grid, Typography } from "@mui/material";
import React, { useEffect, useState } from "react";

const ProjectList: React.FC = () => {
    const [projects, setProjects] = useState<Project[]>([]);
    const getProjects = async () => {
        try {
            const response = await projectApi.getAllProjects();
            setProjects(response?.data);
            console.log("Projects fetched successfully:", response?.data)
        } catch (error) {
            console.error("Error fetching projects:", error);
        }
    };

    useEffect(() => {
        getProjects();
    }, []);

  return (
    <Box sx={{ padding: 2 }}>
  <Grid container spacing={2}>
    {projects.map((project, index) => (
      <Grid size={{xs:12, md:4}} key={index}>
   
                <Card
                  sx={{
                    height: "100%",
                    display: "flex",
                    flexDirection: "column",
                    borderRadius: 3,
                    overflow: "hidden",
                    transition: "all 0.3s ease",
         
                  }}
                >
                  <Box sx={{ position: "relative", overflow: "hidden" }}>
                    <CardMedia
                      component="img"
                      image={
                        project.url || "https://via.placeholder.com/300x250"
                      }
                      alt={project.name}
                      sx={{
                        height: 250,
                        objectFit: "cover",
                        transition: "transform 0.3s ease",
                        "&:hover": {
                          transform: "scale(1.05)",
                        },
                      }}
                    />
                  </Box>

                  <CardContent sx={{ flexGrow: 1, p: 3 }}>
                    <Typography
                      variant="h6"
                      fontWeight="bold"
                      gutterBottom
                      sx={{
                        minHeight: 48,
                        display: "-webkit-box",
                        WebkitLineClamp: 2,
                        WebkitBoxOrient: "vertical",
                        overflow: "hidden",
                      }}
                    >
                      {project.name}
                    </Typography>
                  </CardContent>
                </Card>
          
      </Grid>
    ))}
    </Grid>
    </Box>
  );
}

export default withAuth(ProjectList, {requireAuth:true});