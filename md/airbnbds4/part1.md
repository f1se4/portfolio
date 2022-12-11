#PROJECT DESIGN
This case simulates that we are a real estate company that makes investments in large cities, buying properties to later rent them as tourist apartments.

The management has made the decision to invest in Madrid, and has commissioned us to analyze the data that the leader in the AirBnb sector makes public to try to find the types of properties that have the greatest commercial potential for tourist rentals.

As the main deliverable, they expect the type (or types) of properties that the valuation team must look for among the existing opportunities in the city and the main neighborhoods or geographical areas on which to focus.

To meet the objective we will apply the Discovery methodology and BA techniques.

Although this specific case is focused on tourist rentals, the same type of approach can be used in cases that have a high "location" component:

store opening and closing

reduction of installed capacity

franchise expansion

etc.
## OBJECTIVE
Locate the profile (or profiles) of properties that maximize commercial potential in the tourist rental market and the main areas where to look for them.

## LEVERS
After speaking with the valuation team, they tell us that the levers that have the most impact on the profitability of this type of investment are:

**Rental price:** the more you can charge per night, the higher the profitability

**Occupation:** in general, the more days a year a property can be rented, the greater its profitability

**Real estate price:** the cheaper the property can be acquired, the greater the profitability
## KPI's
In this example the Kpis are pretty straightforward:

- We will measure occupancy as the number of days per year that the property can be rented
- We will measure the rental price as the price per night in euros according to Airbnb
- We will measure the price of a property as the multiplication between the number of square meters and the average price per m2 in your area, and we will apply a 25% discount on the official price due to the negotiation strength of our purchasing team.
## ENTITIES AND DATA
The relevant entities for our objective and from which we may have data are:

Estate

owners

districts

The specific data in each of them will be reviewed in the next module.

## SEED QUESTIONS
### About the rental price:

- What is the average price? And the price range? And by districts? And by neighborhoods?
- What is the ranking of districts and neighborhoods by average rental price?
- What factors (apart from location) determine the rental price?
- What is the relationship between the size of the property and the price for which it can be rented?
- How does the competition (number of properties available per neighborhood) influence the rental price?
- How do the prices vary by rental type (entire flat, private room, shared room)?
### About the occupation:

- What is the average occupancy? And by districts? And by neighborhoods?
- How likely is each occupancy level in each district?
- What is the ranking of districts and neighborhoods by occupation?
- What factors (aside from location) determine occupancy?
- What is the relationship between the size of the property and its degree of occupancy?
- How does competition (number of properties available per neighborhood) influence occupancy?
### About the purchase price:

- What is the price ranking per m2 by district?
- What is the property price ranking (m2 * average size) by district?
- What is the relationship between the price of the property and the rental price by district?
- What is the relationship between the price of the property and the occupation by district?
