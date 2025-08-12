import axiosClient from "../axios-client/axiosClient";

const authApi = {
  login: (data: any) => {
    return axiosClient.post("/login", data);
  },
  signup: (data: { email: string; password: string; name: string }) => {
    return axiosClient.post("/auth/signup", data);
  },
  
}
export default authApi;