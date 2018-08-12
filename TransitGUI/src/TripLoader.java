import org.json.*;

public class TripLoader {
	private final String tripFile = "../apps/schedule_output.json";

	public TripLoader(String trip)
	{
		JSONObject obj = new JSONObject(tripFile);
		JSONArray arr = obj.getJSONArray(trip);
	}
}
