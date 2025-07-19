import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "IMDB Explorer",
  description:
    "Your all-in-one IMDb-powered dashboard—featuring an Actor Profile viewer, Movie Explorer, and Rating Dashboard—designed to deliver fast, intuitive, and structured access to film and celebrity data for both casual viewers and data enthusiasts.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
