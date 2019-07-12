package test.main;

import org.junit.runner.RunWith;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(monochrome = true, plugin = { 
		"junit:target/cucumber-reports" }, features = "features", glue = { "test.stepdefinition" }, tags = { "@mobile1" })
public class TestRunner {

}
