---
description: After the conceptual and logical models are complete, you can make decisions on the physical implementation of the application.
ms.assetid: 18c440f0-88c8-4738-9f29-c82772439b51
title: 'The Physical Model: Application Architecture'
ms.topic: article
ms.date: 05/31/2018
---

# The Physical Model: Application Architecture

After the conceptual and logical models are complete, you can make decisions on the physical implementation of the application. To create the physical model, you must understand where the various services of the application should be located and how they should be implemented. Determining where various services reside should come before how the services will be implemented.

One basic rule for determining where various services reside is this: Put the component where it is being used. If, for example, a component displays information for the base client, it should go on the user's computer. If a component validates information from the base client, it should also reside on the base client's computer. If a component updates information in a database, it should reside on the database server.

There are, of course, additional considerations that make exceptions to this rule. Performance and security issues can also dictate where a component is located. Consider the following:

-   Is a component going to change frequently, making distributing updates difficult?
-   Will the component be used by other applications, such as a common security verification component?
-   Does the component make lengthy calculations or performs functions, such as printing, that can be offloaded to a server?
-   Can the security of a component be enhanced by placing it on a server?

Properly locating components of an application can also insulate the development team from costly recoding if the system or the location of the data changes. For example, by putting the data access rules in a data layer rather than in stored procedures, the application is more easily insulated from dependence on a specific DBMS. Not only are changes confined and testing compartmentalized, but data sources can be changed and data can be distributed without fundamentally changing the application.

Finally, locating components should take advantage of system efficiencies. It is time and cost-effective to place business objects in centralized locations on the network. Objects can be shared among applications, and unit testing can be done before any components are deployed. Maintenance costs can also be decreased because rule changes occur only at a single point.

## Related topics

<dl> <dt>

[The Conceptual Model: Application Requirements](the-conceptual-model--application-requirements.md)
</dt> <dt>

[The Logical Model: Application Definition and Planning](the-logical-model--application-definition-and-planning.md)
</dt> </dl>

 

 



