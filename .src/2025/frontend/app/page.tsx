import Footer from "./globalComponents/footer";
import Header from "./globalComponents/header";

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header
        Home={true}
        ActorProfile={false}
        MovieExplorer={false}
        RatingDashboard={false}
      />
      <main className="flex-1">
        <h1>Home</h1>
      </main>
      <Footer />
    </div>
  );
}
