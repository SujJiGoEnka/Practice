package test.stepdefinition;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

public class Login {
	@Given("^User is on homepage$")
	public void user_is_on_homepage() throws Throwable {
		System.out.println("User is on homepage");
	}

	@Given("^open google\\.com$")
	public void open_google_com() throws Throwable {
		System.out.println("open google\\.com");
	}

	@When("^user search for mobile phones$")
	public void user_search_for_mobile_phones() throws Throwable {
		System.out.println("user search for mobile phones");
	}

	@When("^click on search button$")
	public void click_on_search_button() throws Throwable {
		System.out.println("click on search button");
	}

	@Then("^search result should come on the screen$")
	public void search_result_should_come_on_the_screen() throws Throwable {
		System.out.println("search result should come on the screen");
	}

	@When("^user search for Computer$")
	public void user_search_for_Computer() throws Throwable {
		System.out.println("user search for Computer");
	}

	@When("^user search for \"([^\"]*)\"$")
	public void user_search_for_product(String product) throws Throwable {
		System.out.println("user search for " + product);
	}

}
