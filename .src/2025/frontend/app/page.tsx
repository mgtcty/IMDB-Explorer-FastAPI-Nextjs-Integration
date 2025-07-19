import Header from "./components/header";

export default function Home() {
  return (
    <main>
      <div>
        <Header
          Home={true}
          ActorProfile={false}
          MovieExplorer={false}
          RatingDashboard={false}
        />
        <h1>Home</h1>
      </div>
    </main>
  );
}
