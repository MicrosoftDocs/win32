---
description: The three-tier architecture model, which is the fundamental framework for the logical design model, segments an applications components into three tiers of services.
ms.assetid: a03327c1-e427-4c07-b3d4-808ce81c2c96
title: Using a Three-Tier Architecture Model
ms.topic: article
ms.date: 05/31/2018
---

# Using a Three-Tier Architecture Model

The three-tier architecture model, which is the fundamental framework for the [logical design model](the-logical-model--application-definition-and-planning.md), segments an application's components into three tiers of services. These tiers do not necessarily correspond to physical locations on various computers on a network, but rather to logical layers of the application. How the pieces of an application are distributed in a physical topology can change, depending on the system requirements.

Following are brief descriptions of the services allocated to each tier:

-   **The presentation tier, or user services layer, gives a user access to the application.** This layer presents data to the user and optionally permits data manipulation and data entry. The two main types of user interface for this layer are the traditional application and the Web-based application. Web-based applications now often contain most of the data manipulation features that traditional applications use. This is accomplished through use of Dynamic HTML and client-side data sources and data cursors.

    > [!Note]  
    > In a three-tiered application, the client-side application will be skinnier than a client-server application because it will not contain the service components now located in the middle tier. This results in less overhead for the user, but more network traffic for the system because components are distributed among different machines.

     

-   **The middle tier, or business services layer, consists of business and data rules.** Also referred to as the *business logic tier*, the middle tier is where COM+ developers can solve mission-critical business problems and achieve major productivity advantages. The components that make up this layer can exist on a server machine, to assist in resource sharing. These components can be used to enforce business rules, such as business algorithms and legal or governmental regulations, and data rules, which are designed to keep the data structures consistent within either specific or multiple databases. Because these middle-tier components are not tied to a specific client, they can be used by all applications and can be moved to different locations, as response time and other rules require. For example, simple edits can be placed on the client side to minimize network round-trips, or data rules can be placed in stored procedures.

-   **The data tier, or data services layer, interacts with persistent data usually stored in a database or in permanent storage.** This is the actual DBMS access layer. It can be accessed through the business services layer and on occasion by the user services layer. This layer consists of data access components (rather than raw DBMS connections) to aid in resource sharing and to allow clients to be configured without installing the DBMS libraries and ODBC drivers on each client.

During an application's life cycle, the three-tier approach provides benefits such as reusability, flexibility, manageability, maintainability, and scalability. You can share and reuse the components and services you create, and you can distribute them across a network of computers as needed. You can divide large and complex projects into simpler projects and assign them to different programmers or programming teams. You can also deploy components and services on a server to help keep up with changes, and you can redeploy them as growth of the application's user base, data, and transaction volume increases.

## Related topics

<dl> <dt>

[The Logical Model: Application Definition and Planning](the-logical-model--application-definition-and-planning.md)
</dt> </dl>

 

 



