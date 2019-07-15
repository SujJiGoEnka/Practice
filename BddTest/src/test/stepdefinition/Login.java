package test.stepdefinition;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

public class Login {
	@Given("^User is on homepage$")
	public void user_is_on_homepage() throws Throwable {
		System.out.println("A");
		
	}

	@Given("^open google\\.com$")
	public void open_google_com() throws Throwable {
		System.out.println("B");	
	}

	@When("^user search for \"([^\"]*)\"$")
	public void user_search_for(String arg1) throws Throwable {
		System.out.println(arg1);		
	}

	@When("^click on search button$")
	public void click_on_search_button() throws Throwable {
		System.out.println("D");		
	}

	@Then("^search result should come on the screen$")
	public void search_result_should_come_on_the_screen() throws Throwable {
		System.out.println("E");	
	}

}
