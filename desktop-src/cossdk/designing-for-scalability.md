---
description: Scalability is the ability of an application to service an additional load with a linear increase in resource usage.
ms.assetid: 8249f1af-9c96-4545-ad6a-3736c6e63c6d
title: Designing for Scalability
ms.topic: article
ms.date: 05/31/2018
---

# Designing for Scalability

Scalability is the ability of an application to service an additional load with a linear increase in resource usage. Scalability is important in any distributed application. Limits to scalability usually center around resource use and dependencies inadvertently created in the application's design.

The following list describes scalability issues and suggests solutions:

-   Intra-computer resources. The number of threads and memory available can limit scalability. Use a threading model that is most efficient for your application.
-   Inter-computer resources. The number of available computers to distribute the application workload can affect scalability.
-   Client affinity. Two situations of affinity can be inadvertently created by an application: a situation where the application depends on state from data the client sends with its request; and a situation where the application requires a client-specific state. Avoid designing state dependency between the client and the application.
-   Server affinity. A COM+ application can limit its scalability by creating a server affinity, where the application depends on going to a particular server computer for information. This affinity can occur with many database-oriented applications. The best way to avoid a server-affinity bottleneck is to partition data onto various server computers. For example, divide customer data among servers by the most frequently accessed key, or span a customer database over several servers using the customer's last name (for example, Server1: a-f, Server2: g-m, Server3: n-z).
    > [!Note]  
    > Data partitioning can add a great deal of complexity to the programming logic and should be done only after other options to increase scalability have been tried.

     

-   Object lifetime. To be scalable, a COM+ application must pay close attention to the life span of objects. While an object exists, it is consuming resources. It is important to make sure that the lifetimes of objects that hold onto expensive resources are carefully managed. For high-demand objects that don't consume expensive resources, [COM+ object pooling](com--object-pooling.md) can increase scalability because you can administratively adjust the pooling values to take advantage of whatever hardware you might have. And it's a natural way to govern connections: For example, if you have a license for 20 SQL connections, you can dictate that with the Max Pool setting.
-   Application component grouping. To enhance the scalability of a COM+ application, the middle-tier components should be divided into time-dependent and time-independent services. This allows you to focus on possibly using a Microsoft Windows service to implement a required component action. For example, you could elect to use a service such as [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) or [COM+ queued components](com--queued-components.md) to handle time-independent, asynchronous tasks.

## Related topics

<dl> <dt>

[Designing for Availability](designing-for-availability.md)
</dt> <dt>

[Designing for Deployment](designing-for-deployment.md)
</dt> <dt>

[Designing for Security](designing-for-security.md)
</dt> </dl>

 

 



