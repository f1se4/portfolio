# PROJECT DESIGN

In this case we will be working for a photovoltaic solar power generation company.

Anomalous behaviors have been detected in 2 of the plants and the maintenance subcontractor is unable to identify the reason.

Before deploying a team of engineers, they ask the data science team to analyze the data from the sensors and meters to see if we can detect the problem.

In this case, among other things, we are going to learn:

* how these types of solar plants work
* analysis to be carried out on datasets where the time variable is very important
* how to approach analysis in projects where data is collected by sensors or meters

Therefore, much of what we learn here is generally applicable to industry and IoT projects:

* factory production analysis
* other types of energy
* smart cities
* IoT in agriculture
* etc.


## OBJECTIVE

Analyze the available data to try to intuit where the problems may be and whether or not it is necessary to send a team of engineers to the plants.

## LEVERS

In this type of project in which there is a clear process, the most IMPORTANT part is to know and understand that process.

Let's see, for example, how in this case, which seems easy a priori due to the apparent simplicity of the data, if we do not design the project guided by the process, we could get into an infinite loop of analysis without getting anywhere.

Once we understand how the business and the process work, the levers will come out on their own.

**How does a photovoltaic solar power plant work?**




    
![png](static/notebooks/solar/01_Diseno_del_proyecto_files/01_Diseno_del_proyecto_6_0.png)
    


Therefore, the levers that influence the business objective (in this case, generate AC current) are:

1. **Irradiation**: the greater the irradiation, the greater the DC generated. But it is not monotonic, from certain values higher temperatures can reduce the generation capacity
2. **Condition of the panels**: they must be clean and in good working order to generate the most DC energy possible
3. **Inverter efficiency**: there is always a loss in the transformation from DC to AC, but it must be as little as possible. They must also be in proper condition and working order.
4. **Meters and sensors**: if they break down and do not measure well, we lose traceability and the possibility of detecting failures

## KPI's

* Irradiation: measures the solar energy that arrives
* Ambient and module temperature: measured by plant sensors in degrees Celsius
* DC power: measure the kW of direct current
* AC power: measure the kW of alternating current
* Inverter efficiency (we will create it): measures the capacity of transformation from DC to AC. It is calculated as AC/DC * 100

## ENTITIES AND DATA

To determine the entities it is necessary to know what a solar plant is composed of.

The minimum unit is the cell, it is there where the generation of energy by reaction with the photons of the sun takes place.

The cells are encapsulated in "rectangles" called modules.

Several modules form a panel.

The panels are arranged in rows called arrays.

An inverter receives direct current from several arrays.

A plant can have several inverters.

There are also the meters and sensors, which may be one or more.


    
![jpeg](static/notebooks/solar/01_Diseno_del_proyecto_files/01_Diseno_del_proyecto_13_0.jpg)
    

In our case, the entities that we have in the granularity of the data are:
    
* 15-minute windows over a 34-day period
* Plants: there are 2
* Inverters: several per plant
* Only one irradiation sensor per plant
* Only one room temperature sensor per floor
* Only one module temperature sensor per floor

This conditions that we will be able to know, for example, if an inverter in a plant has lower performance than expected, but we will not know which array, panel or module may be causing it.

## SEED QUESTIONS

Having understood the levers, kpis and entities, we can now ask the seed questions:

About irradiation:

* Is there enough irradiation every day?
* Is it similar on both floors?
* How is your hourly distribution?
* How is it related to ambient temperature and module temperature?

About the plants:

* Does the same amount of irradiation reach them?
* Do they have a similar number of inverters?
* Do they generate similar amounts of DC?
* Do they generate a similar amount of AC?

About the DC generation:

* What is the relationship between irradiation and DC generation?
* Is it ever affected by ambient or module temperature?
* Is it similar on both floors?
* How is it distributed throughout the day?
* Is it constant throughout the days?
* Is it constant in all inverters?
* Have there been moments of failure?

About AC generation:

* What is the relationship between DC and AC generation?
* Is it similar on both floors?
* How is it distributed throughout the day?
* Is it constant throughout the days?
* Is it constant in all inverters?
* Have there been moments of failure?

About meters and sensors:

* Are the irradiation data reliable?
* Is the temperature data reliable?
* Is the DC data reliable?
* Are the CA data reliable?
* Are the data similar between the two plants?