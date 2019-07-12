package com.spring.annotations;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Properties;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.scheduling.annotation.EnableScheduling;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Run {

	@Autowired
	public Hyundai hyundai;

	@Autowired
	public Maruti maruti;

	@Autowired
	Cron c;

	@RequestMapping(value = "/name", method = RequestMethod.POST)
	public void start(@RequestBody Hyundai hyundai1) throws InterruptedException, IOException {

		// ApplicationContext context = new
		// AnnotationConfigApplicationContext(AppConfig.class);
		// Hyundai hyundai = context.getBean(Hyundai.class) ;
		// hyundai.setTime(hyundai1.getTime());
		// hyundai.setType(hyundai1.getType());
		// hyundai.setStartDate(hyundai1.getStartDate());
		hyundai = hyundai1;

		Map<String, String> scheduleParams = new HashMap<String, String>();
		scheduleParams.put("SCHEDULER_TYPE", hyundai.getType());
		scheduleParams.put("TIME", hyundai.getTime());
		scheduleParams.put("START_DATE", hyundai.getStartDate());
		scheduleParams.put("DAY_OF_WEEK", hyundai.getDayWeek());

		// Vehicle accent = context.getBean(Vehicle.class);
		// accent.carConfiguration();
		// Thread.sleep(5000);
		// System.out.println(model);

		maruti.display();

		String s = c.getCronExp(scheduleParams);
		FileOutputStream out = new FileOutputStream("E:/Data.properties");
		Properties props = new Properties();
		props.setProperty("schedule", s);
		props.store(out, null);
		out.close();
		System.out.println("Main method called");

		// hyundai.display();

	}

	@Scheduled(cron = "0 40 12 * * ?")
	public void display() {
		System.out.println("Scheduled");
		if (hyundai.getIsEnabled() == true)
			hyundai.display();

	}

}
