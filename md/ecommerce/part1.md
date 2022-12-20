# PROJECT DESIGN

In this case we will work as consultants for an ecommerce in the cosmetics sector.

This company has had a flat evolution during the last months and has contracted us to analyze its transactional data and implement CRO actions customized to its situation based on said analysis.

In this case, among other things, we are going to learn:

* how are the data of an ecommerce
* Analysis techniques aimed at increasing billing and margin in an e-commerce, both basic or generic, as well as some advanced techniques specific to this sector
* the main metrics on which we have to work and some CRO actions that we can put into practice to improve them
* to build two very powerful analytical resources for this sector: an RFM segmentation and a recommendation system.

Therefore, much of what we learn here is of general application in practically any ecommerce.

## TARGET

Analyze transactional data to try potential CRO actions that increase visits, conversions and average ticket, and therefore increase global ecommerce billing.

Create advanced analytics assets such as RFM segmentation and a recommendation system that drive goal achievement.

## LEVERS

As always, we will first understand the business, and its main processes, metrics and concepts.





    
![png](static/notebooks/ecommerce/part1_files/part1_6_0.png)
    



The first step is when a user arrives at the ecommerce website. It will normally come from:

* Payment campaigns: paid ads such as Facebook Ads or Google Ads
* Organic content: blog, rss, ...
* Direct traffic: knows the url and enters it in the browser

That traffic is called visits, and the pages they see are called page views, although in our case we will call it views.

The user browses the web and when he likes a product, he puts it in the cart.

Finally you can remove products from the cart, leave without buying anything, or finally place the order.

A common process is cross-selling, in which the user is recommended other products that might also interest him.

Even when it's gone we can tell the user again through retargeting or email marketing.

This entire process is called funnel or also customer journey.

In the online environment practically everything can be registered.

The user record can be logged or not.

The sequence of actions that a user does in the same browsing session is called a session.

The ratio of purchases to visits is called the conversion ratio.

In addition, there are other key metrics that we have to master to correctly manage an ecommerce:

* CPA
* AOV
* Purchase frequency
* LTV
* Churn

KEY CONCEPT: There are only 3 ways to grow a business:

1. More customers: this means getting more visits and higher conversion
2. More frequency: this means getting the same customers to buy more times
3. Higher average ticket: this implies getting more or more expensive purchases in the same shopping session

To achieve these 3 effects we work on the following operational levers:

* Customer journey: how we can optimize each step of the process
* Clients: how we can use the information available from clients to optimize the campaigns we carry out
* Products: how we can optimize the product catalog and identify in a personalized way which products we have to put in front of each client

In our case, we will understand CRO in a broad way, that is, as the discipline that puts actions into practice to work on the previous levers and concepts.

## KPI's

* Visits
* Conversion
* Purchase frequency
* Average ticket
* Cart abandonment rate
* LTV

## ENTITIES AND DATA

In our case, the entities that we have in the granularity of the data are:
    
* Users
* Customers
* Sessions
* Events
* Products

## SEED QUESTIONS

Having understood the levers, kpis and entities, we can now ask the seed questions:

About the customer journey:

* What is a typical purchasing process like?
* How many products are viewed, added to cart, abandoned and purchased on average in each session?
* How has the trend of these indicators been in recent months?

About customers:

* How many products does each customer buy?
* How much does each customer spend?
* Are there "better customers" that need to be identified and treated differently?
* Do customers repeat purchases in the following months?
* What is the average LTV of a client?
* Can we design personalized campaigns to customer value?

About the products:

* What are the most sold products?
* Are there products that are not sold?
* Is there a relationship between the price of the product and its sales volume?
* Are there products that are visited but not purchased?
* Are there products that are repeatedly removed from the cart?
* Could personalized product recommendations be made for each client?