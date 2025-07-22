import { Schedule } from "./components/Schedule";

function App() {
  return (
    <div className="max-w-xl mx-auto">
      <h1 className="text-2xl font-bold text-center mt-4 mb-6">
        Расписание рейдов
      </h1>
      <Schedule />
    </div>
  );
}

export default App;
