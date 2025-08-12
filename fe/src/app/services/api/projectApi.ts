import axiosClient from "../axios-client/axiosClient";

const projectApi = {
    getAllProjects : () => {
    return axiosClient.get("/projects");
  }
  
}
export default projectApi;