"use client";

import React from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import { Button, TextField } from "@mui/material";
import authApi from "@/app/services/api/authApi";
import { useRouter } from "next/navigation";
import useAuth from "@/hook/use_auth";
import withAuth from "@/hook/check_auth";
import { jwtDecode } from "jwt-decode";

const validationSchema = yup.object({



  username: yup.string().required("username is required"),
  password: yup
    .string()
    .min(6, "Password should be of minimum 6 characters length")
    .required("Password is required"),
});

const Auth = () => {
    const [errorMessage, setErrorMessage] = React.useState<string | null>(null);
    const navigate = useRouter()
    const { setAuth } = useAuth();

  const formik = useFormik({
    initialValues: {
      username: "foobar@example.com",
      password: "foobar",
    },
    validationSchema: validationSchema,
    onSubmit: async (values) => {
      console.log("Form values:", values);
      try {
              const res = await authApi.login(values);
              const userInfor = res?.data;
              console.log("Login successful:", userInfor);
              localStorage.setItem("userInfor", JSON.stringify(userInfor));
              const decoded: any = jwtDecode(res?.data?.access_token);
              console.log("first", decoded);
              setAuth({
                  user: decoded,
                  accessToken: res?.data?.access_token,
              });
              navigate.replace("/project");

      } catch (error) {
        console.error("Login failed:", error);
        setErrorMessage("Sai tên đăng nhập hoặc mật khẩu");
      }

      
    },
  });

  return (
    <div>
      <form onSubmit={formik.handleSubmit}>
        <TextField
          fullWidth
          id="username"
          name="username"
          label="username"
          value={formik.values.username}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          error={formik.touched.username && Boolean(formik.errors.username)}
          helperText={formik.touched.username && formik.errors.username}
        />
        <TextField
          fullWidth
          id="password"
          name="password"
          label="Password"
          type="password"
          value={formik.values.password}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          error={formik.touched.password && Boolean(formik.errors.password)}
          helperText={formik.touched.password && formik.errors.password}
        />
        <Button color="primary" variant="contained" fullWidth type="submit">
          Submit
        </Button>
      </form>
      <h1>Hile</h1>
    </div>
  );
};

export default withAuth(Auth, {
  requireAuth: false,
});
