/* eslint-disable @typescript-eslint/no-explicit-any */
import axios from "axios";

const axiosClient = axios.create({
  baseURL: `http://localhost:8000/v1`,
  headers: {
    "Content-Type": "application/json",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Origin": "*",
  },
});

axiosClient.interceptors.request.use(
  async (config) => {
    const userDataLocal = localStorage.getItem("userInfor");
    const userData = userDataLocal ? JSON.parse(userDataLocal) : null;
    // console.log("ber: ", userData);
    if (userData) {
      config.headers.Authorization = `Bearer ${userData?.access_token}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);

axiosClient.interceptors.response.use(
  (response) => response.data,
  async (error) => {
    const prevRequest = error?.config;

    if (error?.response?.status === 401 && !prevRequest?.sent) {
      const userDataLocal = localStorage.getItem("userInfor");
      const userData = userDataLocal ? JSON.parse(userDataLocal) : null;

      if (userData) {
        prevRequest.sent = true;

        try {
          const res = await axios.post(
            "/auth/renewtoken",
            {
              refreshToken: userData.tokenModel.refreshToken,
              accessToken: userData.tokenModel.accessToken,
            },
            { baseURL: "http://localhost:8000/v1" }
          );

          const newToken = res?.data?.accessToken;

          if (newToken) {
            const newUserInfor = {
              ...userData,
              tokenModel: {
                refreshToken: userData.tokenModel.refreshToken,
                accessToken: newToken,
              },
            };
            localStorage.setItem("userInfor", JSON.stringify(newUserInfor));

            prevRequest.headers.Authorization = `Bearer ${newToken}`;
            return axios(prevRequest).then((data) => data.data);
          }
        } catch (err: any) {
          console.log(err);
          // handleTokenExpiration();
          return null;
        }
      }
    } 

    return Promise.reject(error);
  }
);

export default axiosClient;
