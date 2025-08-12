import AuthContext from "@/context/auth_context";
import { useContext } from "react";


interface AuthContextType {
  auth: {
    user?: { [key: string]: any };
    accessToken?: string;
  };
  setAuth: React.Dispatch<
    React.SetStateAction<{ user: any; accessToken: any } | {} | null>
  >;
}

const useAuth = () => {
  return useContext(AuthContext) as AuthContextType;
};

export default useAuth;
