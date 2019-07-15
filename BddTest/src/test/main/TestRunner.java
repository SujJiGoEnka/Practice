package test.main;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(monochrome = true, plugin = { 
		"junit:target/cucumber-reports" }, features = {"Features"}, glue={"test.stepdefinition"}, tags = { "@mobile" })
public class TestRunner {

}
