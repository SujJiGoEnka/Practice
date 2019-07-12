
package utilities;
import cucumber.api.java.After;
import cucumber.api.java.Before;
 
public class Hooks {
 @Before
 public void be1foreScenario(){
     System.out.println("This will run before the Scenario");
 } 
 
 @After
    public void afterScenario(){
        System.out.println("This will run after the Scenario");
    }
}