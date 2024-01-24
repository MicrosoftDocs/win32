---
description: 'The Conceptual Model: Application Requirements'
ms.assetid: 124b329b-f745-45b4-b266-7c177c76a5cd
title: 'The Conceptual Model: Application Requirements'
ms.topic: article
ms.date: 05/31/2018
---

# The Conceptual Model: Application Requirements

When designing the conceptual model, you need to define the business problems and the functions required to solve those problems. A best-practices approach is to talk with people who will actually use the application, meet with a broad range of users, and include as many business or user scenarios as possible. Determine the identities and number of the system's potential users, as well as the size and scope of the data involved. Although gathering this information may be the least technical aspect of the design process, it is one of the most important. To develop a successful application, you need a clear understanding of the business problems and processes that need to be addressed.

While determining the application requirements, keep the following considerations in mind:

-   Performance requirements. What is the expected response time for application tasks? What failover support for down servers is needed? What are the hours of availability?
-   Environment. What servers are available? Are additional servers planned to handle any scaling requirements?
-   Deployment. How will the application integrate with a current system? What other systems will the application interact with? What operating systems do the other systems use? What communication protocols should be supported? What API can you use to interact with the other systems? Where are the other systems located on the network? What restrictions on machine use are in place? What user accounts are allowed access?
-   Location. Where is the data located in relation to the client? Is the data remotely accessed, or is it local?
-   Security. Are there encryption or integrity checking requirements? Are there authentication or data protection requirements?
-   Access rights. Are there constraints on who is allowed to perform certain operations? If so, you should first document which operations require authorization and then document the types of users who can have authorization. These requirements can have a big impact on how parts of the application are implemented.

## Related topics

<dl> <dt>

[The Logical Model: Application Definition and Planning](the-logical-model--application-definition-and-planning.md)
</dt> <dt>

[The Physical Model: Application Architecture](the-physical-model--application-architecture.md)
</dt> </dl>

 

 



