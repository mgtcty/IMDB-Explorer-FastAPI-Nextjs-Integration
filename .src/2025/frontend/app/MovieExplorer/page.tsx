import React from "react";
import Header from "../globalComponents/header";
import Footer from "../globalComponents/footer";

const MovieExplorer = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header Home={false} ActorProfile={false} MovieExplorer={true} />

      <main className="flex-1">MovieExplorer</main>

      <Footer />
    </div>
  );
};

export default MovieExplorer;
