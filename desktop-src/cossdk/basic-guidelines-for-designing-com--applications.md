---
description: Basic Guidelines for Designing COM+ Applications
ms.assetid: 2d08bd05-5b0c-480c-91fd-b2bf321fc21e
title: Basic Guidelines for Designing COM+ Applications
ms.topic: article
ms.date: 05/31/2018
---

# Basic Guidelines for Designing COM+ Applications

To take full advantage of COM+, there are a few basic guidelines you can use when creating an application:

-   **Model your durable state as a database schema, using your database tool of choice.** Almost every application needs to maintain durable state. Databases provide the services needed to create durable and scalable storage of state. Therefore, the first step in creating a COM+ application is to model the durable state of your application as some sort of database schema. It doesn't really matter what database you use; most commercial databases are compatible with COM+. Microsoft SQL Server is a good example of one solution you could use.

-   **Model the logic of your COM+ application as a set of COM interfaces.** Once you have a schema that represents the state information of the application, model the interchanges that happen in the application as COM interfaces. These interfaces will model the behavior of the application. This is also the development stage when you should determine which COM+ services work best for your application.

-   **Build component DLLs that contain components that use the physical data schema and expose a logical view of the data to other components (the first item in this list), as well as components that are implemented in terms of the logical data model (the second item in this list).** Once you have the structure of the logic and the state information, you can begin to write code and can now write DLL-based COM components that implement the interfaces in terms of the defined schema. Your components simply act as manipulators for working with your database information, and your component DLLs enable you build a COM+ application that works and that scales successfully.

-   **Deploy the components in the COM+ environment using the COM+ services you've selected.** Once you have built the application, you can then deploy the application across a network or server cluster. You can now make decisions based on resources available, and you can tailor each component for maximum performance.

## Related topics

<dl> <dt>

[COM+ Design Assumptions and Principles](com--design-assumptions-and-principles.md)
</dt> <dt>

[Designing the COM+ Application Using UML](designing-the-com--application-using-uml.md)
</dt> <dt>

[General Design Tips for Using COM+](general-design-tips-for-using-com-.md)
</dt> <dt>

[Optimizing Interactions with the COM+ Business Logic Tier](optimizing-interactions-with-the-com--business-logic-tier.md)
</dt> <dt>

[Other Microsoft Tools for Building Distributed Applications](other-microsoft-tools-for-building-distributed-applications.md)
</dt> </dl>

 

 



