package com.spring.annotations;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.scheduling.annotation.EnableScheduling;


@PropertySource("classpath:RequestData.Properties")
@Configuration
@ComponentScan(basePackages="CronExample")
@EnableScheduling
public class AppConfig {

}
