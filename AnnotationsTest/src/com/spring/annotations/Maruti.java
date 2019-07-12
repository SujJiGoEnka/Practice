package com.spring.annotations;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
@PropertySource("Data.properties")
public class Maruti {
	private String cost;
	private String model = null;

	@Value("${cost}")
	public void setCost(String cost) {
		this.cost = cost;
	}

	@Value("Mustang")
	public void setModel(String model) {
		this.model = model;
	}

	public void display() {
		System.out.println("The model is " + this.model + " with cost " + this.cost);

	}

}
