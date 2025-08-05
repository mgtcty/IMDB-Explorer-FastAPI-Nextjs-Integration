import React from "react";
import Footer from "../globalComponents/footer";
import Header from "../globalComponents/header";

const ActorProfile = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header
        Home={false}
        ActorProfile={true}
        MovieExplorer={false}
        RatingDashboard={false}
      />
      <main className="flex-1">ActorProfile</main>
      <Footer />
    </div>
  );
};

export default ActorProfile;
