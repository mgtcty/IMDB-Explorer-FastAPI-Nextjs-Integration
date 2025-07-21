import React from "react";
import Header from "../components/header";
import Footer from "../components/footer";

const MovieExplorer = () => {
  return (
    <div>
      <Header
        Home={false}
        ActorProfile={false}
        MovieExplorer={true}
        RatingDashboard={false}
      />
      MovieExplorer
      <Footer />
    </div>
  );
};

export default MovieExplorer;
