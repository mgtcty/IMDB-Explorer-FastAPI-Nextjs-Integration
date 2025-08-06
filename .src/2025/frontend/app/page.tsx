import Footer from "./globalComponents/footer";
import Header from "./globalComponents/header";

interface topFivePeople {
  name: String;
  role: String[];
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

  // table content
  const tableContentPeople = topPeople ? (
    topPeople.map((people, index) => (
      <tr>
        <td>{people.name}</td>
        <td>{people.role?.join(", ")}</td>
        <td>{people.count}</td>
      </tr>
    ))
  ) : (
    <tr>
      <td>Cant display Name</td>
      <td>Cant display Role</td>
      <td>Cant display Count</td>
    </tr>
  );

  const tableContentMovies = topMovies ? (
    topMovies.map((movie, index) => (
      <tr>
        <td>{movie.movieName}</td>
        <td>{movie.genre}</td>
        <td>{movie.rating}</td>
      </tr>
    ))
  ) : (
    <tr>
      <td>Cant display Title</td>
      <td>Cant display Genre</td>
      <td>Cant display Rating</td>
    </tr>
  );

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
            <tbody>{tableContentMovies}</tbody>
          </table>
        </div>
        <div>
          <h2>Top 5 Most Known People</h2>
          <table>
            <thead>
              <tr>
                <th>Actor/Actress</th>
                <th>Role</th>
                <th>Count</th>
              </tr>
            </thead>
            <tbody>{tableContentPeople}</tbody>
          </table>
        </div>
      </main>
      <Footer />
    </div>
  );
}
