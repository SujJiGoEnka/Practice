package com.spring.annotations;

import javax.ws.rs.core.Application;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

@RequestMapping
public class Run {

	public void start(@RequestBody Hyundai hyundai) {

		// Code used for XML based configuration
		/*
		 * ApplicationContext context = new
		 * ClassPathXmlApplicationContext("bean.xml"); Vehicle accent =
		 * context.getBean("vehicle", Vehicle.class); accent.carConfiguration();
		 */

		ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
		Vehicle accent = context.getBean(Vehicle.class);
		accent.carConfiguration();

	}

}
