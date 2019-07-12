package com.spring.annotations;

import org.springframework.stereotype.Component;

@Component
public class Hyundai {

	private String type;
	private String time;
	private String startDate;
	private String dayWeek;
	private Boolean isEnabled = false;
	
	
	public Boolean getIsEnabled() {
		return isEnabled;
	}

	public void setIsEnabled(Boolean isEnabled) {
		this.isEnabled = isEnabled;
	}

	public String getStartDate() {
		return startDate;
	}

	public void setStartDate(String startDate) {
		this.startDate = startDate;
	}

	public String getDayWeek() {
		return dayWeek;
	}

	public void setDayWeek(String dayWeek) {
		this.dayWeek = dayWeek;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getTime() {
		return time;
	}

	public void setTime(String time) {
		this.time = time;
	}

	public void display() {
		System.out.println("Schedule Type is " + this.type + " and the time is " + this.time);

	}

}
