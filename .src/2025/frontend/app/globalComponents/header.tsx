import Link from "next/link";
import React from "react";

interface IsInPage {
  ActorProfile: boolean;
  MovieExplorer: boolean;
  Home: boolean;
}

const Header = (props: IsInPage) => {
  const isInPage = props;
  const link = (isInPage: boolean, pageName: string, pageTitle: string) => {
    return (
      <div>
        {isInPage ? (
          <Link href={pageName}>{pageTitle}</Link>
        ) : (
          <span className="text-gray-400">{pageTitle}</span>
        )}
      </div>
    );
  };

  return (
    <div className="flex items-center justify-center gap-12 m-6">
      {link(!isInPage.Home, "/", "Home")}
      {link(!isInPage.MovieExplorer, "/MovieExplorer", "Movies")}
      {link(!isInPage.ActorProfile, "/ActorProfile", "Actors")}
    </div>
  );
};

export default Header;
