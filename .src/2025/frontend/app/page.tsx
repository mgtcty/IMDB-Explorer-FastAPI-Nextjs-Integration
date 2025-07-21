import Footer from "./globalComponents/footer";
import Header from "./globalComponents/header";

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
        <Footer />
      </div>
    </main>
  );
}
