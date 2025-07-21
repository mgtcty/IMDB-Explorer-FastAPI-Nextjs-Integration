import React from "react";
import { DatabaseIcon } from "./IconsSvg";

const Footer = () => {
  return (
    <footer className="footer sm:footer-horizontal bg-amber-500 text-amber-950 p-10">
      <aside>
        <DatabaseIcon params="text-amber-950 w-12 h-12" />
        <p>
          IMDB Explorer.
          <br />
          This project is for educational purposes only. It is not affiliated
          <br />
          with IMDb. Some data is sourced from IMDb but is not used for
          <br />
          commercial purposes.
        </p>
      </aside>
    </footer>
  );
};

export default Footer;
