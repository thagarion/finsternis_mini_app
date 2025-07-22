import React, { useEffect, useState } from "react";

interface EventItem {
  type: string;
  time_local: string;
  in: string;
  channels: number[];
}

const apiUrl = process.env.REACT_APP_API_URL || "http://localhost:8000";

export const Schedule = () => {
  const [events, setEvents] = useState<EventItem[]>([]);

  useEffect(() => {
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
    fetch(`${apiUrl}/schedule?tz=${tz}`)
      .then((res) => res.json())
      .then((data) => setEvents(data));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Ближайшие события</h2>
      <ul className="space-y-2">
        {events.map((event, index) => (
          <li
            key={index}
            className="bg-gray-100 p-3 rounded shadow flex flex-col gap-1"
          >
            <div className="font-semibold capitalize">{event.type}</div>
            <div>⏰ {event.time_local} ({event.in} осталось)</div>
            <div>🔀 Каналы: {event.channels.join(", ")}</div>
          </li>
        ))}
      </ul>
    </div>
  );
};