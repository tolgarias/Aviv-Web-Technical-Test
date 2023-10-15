# AVIV technical test solution

You can use this file to write down your assumptions and list the missing features or technical revamp that should
be achieved with your implementation.

## Notes

Write here notes about your implementation choices and assumptions.

I picked up python as a language because I've told that the project that will be assigned to me will be in python.
Implementation took around 4 hours due to the fact that I don't have much experience with python.

I didn't update the [sql migration files](/db)  because I had `docker-compose` issues on my machine and I couldn't run
Also i didn't update [listings.yaml](listings.yaml).
the application.

## Questions

This section contains additional questions your expected to answer before the debrief interview.

- **What is missing with your implementation to go to production?**
My changes should be reviewed by another engineer and approved before merging them to the main branch.

- **How would you deploy your implementation?**
   - Merge changes to the main branch
   - CDP triggers a build on the main branch, run the unit and integration tests
   - CDP deploys the application to the staging environment
   - QA team tests the application
   - Application is deployed to production

- **If you had to implement the same application from scratch, what would you do differently?**

First of all `listing` data structure is missing owner of the listing. 
I would add `owner` to the `listing` table to to make sure only owner of the listing can update it.
I would add authorization to the listing api with a token to increase security.
Probably I'd use a NoSQL database like `DynamoDB` to avoid join operations on database tables. That'd be helpful to add clustering to the database if it's needed.
And a good to have thing would be creating api endpoints from the `listing.yaml` file to ensure it's updated.

- **The application aims at storing hundreds of thousands listings and millions of prices, and be accessed by millions
  of users every month. What should be anticipated and done to handle it?**

I'd put listing api's to a load balancer to handle millions of requests. 
PostgreSQL can handle millions of records but if clustering can be added to the database if it's needed. 
`listing_id` in the `listing_history` might be indexed to make sure that the query will be fast.  

  NB : You can update the [given architecture schema](./schemas/Aviv_Technical_Test_Architecture.drawio) by importing it
  on [diagrams.net](https://app.diagrams.net/) 
