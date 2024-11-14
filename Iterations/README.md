# Iterations

This is where my backup copies/iterative versions will live, numbered clearly so as to be self-explanatory.

Each filename is structured as such:
fc = FlightCal
It = iteration
[number] = iteration number
(yyyy.mm.dd) = date of completion.

Which all comes out to be:
fcItX(yyyy.mm.dd).py

## Iterations

- fcIt1(2024.09.24).py
    - Destinations (3)
    - Age Discounts
    - Final Cost Output
    - Seat-Based Cost
- fcIt2(2024.10.01).py
    - Destinations (3)
    - Age Discounts
    - Final Cost Output
    - Seat-Based Cost
    - Class Difference
- fcIt3(2024.10.16).py
    - Destinations (6)
    - Age Discounts
    - Final Cost Output
    - Seat-Based Cost
    - Class Difference
    - Email Output
- fcIt4(2024.11.06).py
    - Destinations (6)
    - Age Discounts
    - Final Cost Output
    - Seat-Based Cost
    - Class Difference
    - Email Output
    - XML Data Output
    - XML Data Retrieval

## Item Descriptions

- Destinations (x)
    - In FlightCal, there are a number of destinations; i.e places to go to. x is how many destinations are in each iteration of the app.
    - Destinations are applied as the initial cost from which everything is based off of, as fuel, catering, and hiring costs are the main variables, but these are constant as they'll be the same distance from the airport using the app, and therefore they can be consolidated into one destination cost. This is also convenient because now all the other variables about the customer can be applied reliably onto a base without worry.
- Age Discounts
    - This models the costs via age, in this program for example, I have an elderly discount (60+) for 20% off, and a teen/child discount (-18) for 15% off.
    - This is the stand-in for something such as a supergold card or similar. It also exists to model the current airline systems where children have cheaper seats, except to entice the customer it's modelled as a discount instead of a lower base.
- Final Cost Output
    - This is the item that spits out the final cost of the trip for the client. 
    - This shows that the final_cost_resolver definition is complete and functioning correctly, and I can compare it to my algebraic planning for correctness.
    - It's not an email output, it is just the number.
- Seat-Based Cost
    - This is an alteration of the cost based on the amount of seats left.
    - I've set it up so that the seat discount is the amount of seats divided by the amount of seats left
- Class Difference
    - This is the application of the difference in cost between the flight classes, such as Economy or Business.
    - This is implemented by simply multiplying the base cost, defined by the destination, by a small value such as 1.2, or 2.
- Email Output
    - This is the output of the program, the main reason for it's existence. This output provides simply a copy-pastable email utilizing all the values from earlier, for the travel agent to send to the client.
- XML Data Output
    - This takes the information you've taken about the client, and outputs it into an xml file for later retrieval.
- XML Data Retrieval
    - This takes data within the xml file which was written earlier, and shows it to the user again in elegant formatting.

## Tests

### Test Descriptions

- Age Boundary Test
    - This test will show that the minimum age input is 1, and that the maximum is 160. It will also make sure that the program does not break or fail when given values that exceed or go under the maximum and minimum respectively. 
    - With this test I will put the age at 0, 1, 2, 159, 160, 161, and 248 in 7 separate runs of the program.
    - I expect 0, 161, and 248 to trigger a re-entry of the client's age.
- Destination Input Error Test
    - This test will show that when inputting the number of the destination within the program, that numbers exceeding or under the range shown will not break the program and instead simply provide an error message.
    - With this test I will input numbers 0, 1, 3, 4, 6, and 7 in 7 separate runs of the program.
    - For fcIt1-2, I expect 0, 4, 6, and 7 to trigger a re-entry,
    - and for fcIt3-4, I expect 0 and 7 to trigger a re-entry.
- Class Input Error Test
    - This test will show that when inputting the number of the class within the program, that numbers exceeding or under the range shown will not break the program and instead simply provide an error message.
    - With this test I will input numbers 0, 1, 2, 4, and 5 in 6 separate runs of the program.
    - I expect 0 and 5 to trigger a re-entry of the class.
- Name Input Correction Test
    - This test will show that when the Flight Attendant inputs a name, it will be automatically capitalised and reformatted, and that if they input a number within the name it will force a re-entry and not be displayed.
    - I will enter the names “john hank”, “h4nk g13nn”, and “H314 R1ch4Rds0n” in three separate runs of the program.
    - I will expect the program to recognize that the last two names are invalid and ask for the name again, and for “john hank”, it should output “John Hank” in the final output.
- Remaining Seat Input Test
    - This test will show that the program can recognize when the count of remaining seats is higher than the count of seats available, and prompt a re-entry.
    - For this I will enter the numbers 199, 250, and 251 in 3 separate program runs to test the boundary of the seat count, teasing the global maximum of 250.
    - I will expect the program to inform me of this discrepancy and a re-entry prompt to be displayed.
- Data Save Test
    - After entering the information for a client, the client data is saved in an external xml file.
    - This test will show that the xml file is being successfully written to and isn't having issues. I will simply input the default values listed below, and parse `flight_data.xml` for the values inputted.
    - I expect the program to save the client data, and to output `Data for Hank Fret saved to flight_data.xml`
- Data Retrieval Test
    - For this test, inside the program I will run the 'Retrieve Client Data' option, and retrieve the data from the test above.
    - I expect 2 tables with 4 values each to be printed. One for cost and one for info. I also expect that before the program shuts down, it will run the email function, writing our client's output email again. 
- Algebra Test
    - For this test, I will be checking my calculation of the final cost and making sure it is what I intended it to be.
    - I expect that using the default values below, the final cost should be $144.
- Data Clear Test
    - This tests my function to delete the client data, i.e the xml file.
    - I will simply press 3 at the start menu of the program to trigger the data removal, and et voila, `flight_data.xml` should cease to exist.

### Default Testing Values
#### Name
- Hank Fret
#### Age
- 43
#### Destination
- 3 (Wellington)
#### Class
- 2 (Premium Economy)
#### Remaining Seats
- 143
#### Expected Cost Output
- 200*1.2\*0.6 = $144

### Testing

Success indicates that the iteration passed the test,
N/A indicates that the feature wasn't implemented in that iteration.

|                              |  fcIt1  |  fcIt2  |  fcIt3  |  fcIt4  |
|------------------------------|---------|---------|---------|---------|
| Age Boundary Test            | Success | Success | Success | Success |
| Destination Input Error Test | Success | Success | Success | Success |
| Algebra Test                 | Success | Success | Success | Success |
| Class Input Error Test       |   N/A   | Success | Success | Success |
| Name Input Correction Test   |   N/A   |   N/A   | Success | Success |
| Remaining Seat Input Test    | Success | Success | Success | Success |
| Data Save Test               |   N/A   |   N/A   |   N/A   | Success |
| Data Retrieval Test          |   N/A   |   N/A   |   N/A   | Success |