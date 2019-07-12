package CronExample;

import java.util.*;

import com.spring.annotations.Cron;

import java.io.*;

public class Config {
	static Properties prop = new Properties();
	

//	public static RequestVariables addConfig() throws IOException {
//		RequestVariables requestVariables = new RequestVariables();
//		Properties prop = new Properties();
//		ClassLoader loader = Thread.currentThread().getContextClassLoader();
//		InputStream stream = loader.getResourceAsStream("RequestData.properties");
//		prop.load(stream);
//		requestVariables.setYear(prop.getProperty("Year"));
//		requestVariables.setJurisOrgGroupId(Integer.parseInt(prop.getProperty("JurisOrgGroupId")));
//		requestVariables.setMaxRecords(Integer.parseInt(prop.getProperty("MaxRecords")));
//
////		System.out.println(requestVariables.getYear());
//		return requestVariables;
//
//	}

	public static final String scheduleParams() throws IOException {
		Properties prop = new Properties();
		ClassLoader loader = Thread.currentThread().getContextClassLoader();
		InputStream stream = loader.getResourceAsStream("RequestData.properties");
		prop.load(stream);
		Map<String, String> scheduleParams = new HashMap<String, String>();
		scheduleParams.put("SCHEDULER_TYPE", prop.getProperty("SCHEDULER_TYPE"));
		scheduleParams.put("TIME", prop.getProperty("TIME"));
		scheduleParams.put("START_DATE", prop.getProperty("START_DATE"));
		scheduleParams.put("DAY_OF_WEEK", prop.getProperty("DAY_OF_WEEK"));
		Cron c = new Cron();
		return c.getCronExp(scheduleParams);

	}
}
