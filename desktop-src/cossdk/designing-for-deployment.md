---
description: Designing for Deployment
ms.assetid: 31244998-34f5-4fd8-95f6-adcc134bcaf3
title: Designing for Deployment
ms.topic: article
ms.date: 05/31/2018
---

# Designing for Deployment

Planning the scope of COM+ applications is an important design task you should consider early on. Distributed systems that are intended to run using COM+ should be designed for deployment with the least amount of individual configuration and to most efficiently use each process. There are also techniques you can use that will enable you to achieve optimal performance when deploying a COM+ application. (For more information, see [Deploying for Faster Communication](deploying-for-faster-communication.md).)

When viewed with the Component Services administrative tool, each COM+ application appears as a folder within which sets of components are logically grouped. While you can move individual components between COM+ application **Components** folders (in other words, from one application to another), several services set at the COM+ application level, such as security, may differ. These service settings can affect portability.

## A COM+ Server Application Defines a Process Boundary

When you create a new COM+ server application, you are really defining a new process boundary. (Note the exception for library applications explained below.) This process becomes the controlling application instance for the components that are contained in the COM+ application. These components all run in-process in a new instance of the COM+ executable program whenever a program calls into a COM+ application for the first time. This means that all of the components within a given COM+ application's **Components** folder run in a single process space that serves as the DCOM server. Within the COM+ application, COM+ manages memory, coordination with the Distributed Transaction Coordinator (DTC), just-in-time component instance activation, crash detection and recovery, and role-based security.

## Calling Across COM+ Application Boundaries

Because each COM+ application normally is implemented as a separate executable, the effect of splitting a distributed application across multiple COM+ applications introduces out-of-process COM calls when components in one COM+ application call the components in another COM+ application. This introduces performance degradation due to the extra burden that marshaling COM parameters across processes imposes.

> [!Note]  
> There is nothing inherently wrong with incurring this performance penalty; you just need to be aware that it is going to occur. Depending on the required response time, the number of users that will simultaneously request business services, and the added start-up burden that each component adds to each COM+ application, you may find that the performance hit attributable to cross-application calls is acceptable.

 

One possibility that eliminates the performance penalty of calling across COM+ application boundaries is to mark a given COM+ application as a library application. A COM+ library application runs in the process of the client that creates it. Of course, no performance gain has zero cost. In this case, the trade-off involves the limitations of COM+ library applications. While a library application can use role-based security, it cannot support queued components or remote access.

## Related topics

<dl> <dt>

[Deploying for Faster Communication](deploying-for-faster-communication.md)
</dt> <dt>

[Designing for Availability](designing-for-availability.md)
</dt> <dt>

[Designing for Scalability](designing-for-scalability.md)
</dt> <dt>

[Designing for Security](designing-for-security.md)
</dt> </dl>

 

 



