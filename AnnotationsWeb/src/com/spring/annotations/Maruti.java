package com.spring.annotations;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

@Component
public class Maruti {

	@Autowired
	private Hyundai hyundai;
	
	private String cost;
	private String model = null;
	

	public String getCost() {
		return cost;
	}

	public String getModel() {
		return model;
	}

	public void setCost(String cost) {
		this.cost = cost;

	}

	public void setModel(String model) {
		this.model = model;
	}

	public void display() {
//		System.out.println("The model is " + this.model + " with cost " + this.cost);
		System.out.println("In calss Maruti-->" + hyundai.getTime());
		System.out.println("In calss Maruti-->" + hyundai.getStartDate());
		System.out.println("In calss Maruti-->" + hyundai.getDayWeek());
		System.out.println("In calss Maruti-->" + hyundai.getClass());
		System.out.println("In calss Maruti-->" + hyundai.getStartDate());
	}

}
