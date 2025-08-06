import Footer from "./globalComponents/footer";
import Header from "./globalComponents/header";

interface topFivePeople {
  name: String;
  roles: String[];
  count: number;
}

interface topFiveMovies {
  movieName: String;
  genre: String;
  rating: Float16Array;
}

export default async function Home() {
  // Get the top 5 movies (highest rating)
  const resPeople = await fetch("http://127.0.0.1:8000/top5_people");
  // Get the top 5 people (most appearance in database)
  const resMovies = await fetch("http://127.0.0.1:8000/top5_movies");

  const topPeople: topFivePeople[] = await resPeople.json();
  const topMovies: topFiveMovies[] = await resMovies.json();

  return (
    <div className="min-h-screen flex flex-col">
      <Header Home={true} ActorProfile={false} MovieExplorer={false} />
      <main className="flex-1">
        <h1>Explore movies and actors from IMDb dataset</h1>
        <div>
          <h2>Top 5 Rated Movies</h2>
          <table>
            <thead>
              <tr>
                <th>Movie Name</th>
                <th>Genre</th>
                <th>Rating</th>
              </tr>
            </thead>
            <tbody>
              {topMovies.map((movie, index) => (
                <tr key={index}>
                  <td> {movie.movieName} </td>
                  <td> {movie.genre} </td>
                  <td> {movie.rating} </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <div>
          <h2>Top 5 Most Known People</h2>
          <table>
            <thead>
              <tr>
                <th>Actor/Actress</th>
                <th>Role</th>
              </tr>
            </thead>
            <tbody></tbody>
          </table>
        </div>
      </main>
      <Footer />
    </div>
  );
}
