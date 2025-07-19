import Link from "next/link";
import React from "react";
import { IsInPage } from "@/types/Routing";

const Header = (page: IsInPage) => {
  const isInPage: IsInPage = page;
  const link = (isInPage: boolean, pageName: string, pageTitle: string) => {
    return (
      <div>
        {isInPage ? (
          <Link href={pageName}>{pageTitle}</Link>
        ) : (
          <text className="text-gray-400">{pageTitle}</text>
        )}
      </div>
    );
  };

  return (
    <div className="flex items-center justify-between gap-4">
      {link(!isInPage.Home, "/", "Home")}
      {link(!isInPage.MovieExplorer, "/MovieExplorer", "Movies")}
      {link(!isInPage.ActorProfile, "/ActorProfile", "Actors")}
      {link(!isInPage.RatingDashboard, "/RatingDashboard", "Dashboard")}
    </div>
  );
};

export default Header;
