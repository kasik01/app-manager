"use client";
import { createContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";

const AuthContext = createContext({});

interface AuthProviderProps {
  children: React.ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [auth, setAuth] = useState({ user: {}, accessToken: "" });

  useEffect(() => {
    if (typeof window !== "undefined") {
      const jsonString = localStorage.getItem("userInfor");
      const userStorage = jsonString ? JSON.parse(jsonString) : null;
      const storedAccessToken = userStorage?.access_token;

      if (storedAccessToken) {
        try {
          const decoded = jwtDecode(storedAccessToken);
          setAuth({ user: decoded, accessToken: storedAccessToken });
        } catch (error) {
          console.error("Lỗi giải mã token:", error);
          setAuth({ user: {}, accessToken: "" });
        }
      }
    }
  }, []); // Chạy một lần sau khi component mount

  return (
    <AuthContext.Provider value={{ auth, setAuth }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
