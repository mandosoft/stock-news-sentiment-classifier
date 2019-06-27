import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;



public class ParseJSON {

  //change the path as per requirement
	public static final String CSV_FILE_NAME= "/Users/mangeshkalsulkar/Desktop/stocks.csv";

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub

		String path="/Users/mangeshkalsulkar/Desktop/stocks.json";
		Map<String,String> titlesMap= new HashMap<String,String>();
		List<String[]> dataLines = new ArrayList<>();
		ParseJSON parseJSON= new ParseJSON();


	  try(FileReader reader= new FileReader(path)){

			JsonParser jsonParser= new JsonParser();
			JsonElement jsonElement= jsonParser.parse(reader);
			JsonObject jsonObject= jsonElement.getAsJsonObject();

			JsonArray jsonArray= jsonObject.get("articles").getAsJsonArray();
			System.out.println(jsonArray.size());


			for(int i=0;i<jsonArray.size();i++){

				JsonObject obj= jsonArray.get(i).getAsJsonObject();
				String title=obj.get("title").getAsString();
				String publishedDate=obj.get("publishedAt").getAsString();
				publishedDate=(publishedDate.contains("T"))?publishedDate.split("T")[0]:publishedDate;
                titlesMap.put(title, publishedDate);
                dataLines.add(new String[] {title,publishedDate});

			}

		}

//	  System.out.println("Map is:"+dataLines);
	  parseJSON.givenDataArray_whenConvertToCSV_thenOutputCreated(dataLines);

	}

	public  void givenDataArray_whenConvertToCSV_thenOutputCreated(List<String[]> dataLines) throws IOException {
	    File csvOutputFile = new File(CSV_FILE_NAME);
	    try (PrintWriter pw = new PrintWriter(csvOutputFile)) {
	        dataLines.stream()
	          .map(this::convertToCSV)
	          .forEach(pw::println);
	    }

	}

	public String convertToCSV(String[] data) {
	    return Stream.of(data)
	      .map(this::escapeSpecialCharacters)
	      .collect(Collectors.joining(","));
	}

	public String escapeSpecialCharacters(String data) {
	    String escapedData = data.replaceAll("\\R", " ");
	    if (data.contains(",") || data.contains("\"") || data.contains("'")) {
	        data = data.replace("\"", "\"\"");
	        escapedData = "\"" + data + "\"";
	    }
	    return escapedData;
	}

}
