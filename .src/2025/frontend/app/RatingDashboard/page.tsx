import React from "react";
import Header from "../components/header";
import Footer from "../components/footer";

const RatingDashboard = () => {
  return (
    <div>
      <Header
        Home={false}
        ActorProfile={false}
        MovieExplorer={false}
        RatingDashboard={true}
      />
      RatingDashboard
      <Footer />
    </div>
  );
};

export default RatingDashboard;
