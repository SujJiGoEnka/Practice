package CronExample;

import java.util.Date;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import com.spring.annotations.AppConfig;

@Component
public class DemoService {

	@Scheduled(cron = "${batch.name}")
	public void demoServiceMethod() {
		System.out.println("Method executed at every 5 seconds. Current time is :: " + new Date());
	}

	public static void main(String[] args) {
		ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
		System.out.println("hi");
	}
}