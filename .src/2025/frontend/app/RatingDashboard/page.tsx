import React from "react";
import Header from "../globalComponents/header";
import Footer from "../globalComponents/footer";

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
