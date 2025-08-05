import React from "react";
import Header from "../globalComponents/header";
import Footer from "../globalComponents/footer";

const RatingDashboard = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header
        Home={false}
        ActorProfile={false}
        MovieExplorer={false}
        RatingDashboard={true}
      />
      <main className="flex-1">RatingDashboard</main>
      <Footer />
    </div>
  );
};

export default RatingDashboard;
