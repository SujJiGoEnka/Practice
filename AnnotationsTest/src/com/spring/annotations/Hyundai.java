package com.spring.annotations;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
public class Hyundai {

	private String model;
	private String cost;

	public void setCost(String cost) {
		this.cost = cost;
	}

	public void setModel(String model) {
		this.model = model;
	}

	public void display() {
		System.out.println("The model is " + this.model + " and the cose is " + cost);

	}

}
