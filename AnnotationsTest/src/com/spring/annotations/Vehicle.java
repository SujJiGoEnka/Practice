package com.spring.annotations;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Vehicle {

	@Autowired
	private Hyundai hyundai;
	@Autowired
	private Maruti maruti;

	private String status;

	public void setMaruti(Maruti maruti) {
		this.maruti = maruti;
	}

	public void setStatus(String status) {
		this.status = status;
	}

	public void setHyundai(Hyundai hyundai) {
		this.hyundai = hyundai;
	}

	public void carConfiguration() {
		hyundai.display();
		maruti.display();
		System.out.println("Status: " + this.status);
	}
}
