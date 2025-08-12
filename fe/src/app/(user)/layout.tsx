'use client';

import { Box } from "@mui/material";
import dynamic from "next/dynamic";
const AuthProviderClientOnly = dynamic(
  () => import("../../context/auth_context").then((mod) => mod.AuthProvider),
  { ssr: false }
);

export default function UserLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <>
    <AuthProviderClientOnly>
      <Box>
        {children}
      </Box>
    </AuthProviderClientOnly>
    </>
  );
}