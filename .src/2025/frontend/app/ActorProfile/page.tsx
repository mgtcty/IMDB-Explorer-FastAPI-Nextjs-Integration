import React from "react";
import Footer from "../components/footer";
import Header from "../components/header";

const ActorProfile = () => {
  return (
    <div>
      <Header
        Home={false}
        ActorProfile={true}
        MovieExplorer={false}
        RatingDashboard={false}
      />
      ActorProfile
      <Footer />
    </div>
  );
};

export default ActorProfile;
