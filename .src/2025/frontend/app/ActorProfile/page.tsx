import React from "react";
import Footer from "../globalComponents/footer";
import Header from "../globalComponents/header";

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
