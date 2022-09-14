---
description: Availability is the ability of an application to tolerate failures in server resources.
ms.assetid: 5d9a8216-a568-4443-b94f-1b2f2827a4be
title: Designing for Availability
ms.topic: article
ms.date: 05/31/2018
---

# Designing for Availability

Availability is the ability of an application to tolerate failures in server resources. This means that the client continues to be served through the failure and that, ideally, the failure is transparent to the client. Obviously, the failure can come from either hardware or software sources, so you must develop for both cases.

Availability can be affected by the following factors:

-   Application model. For highest availability, ensure that the critical application logic is conducted using the [COM+ transactions](com--transactions.md) service. In addition, using a compensation mechanism can be effective in ensuring that resources remain in a healthy state after failures.
-   Client model. Integrate "retry on failure" logic into the client application, and strive for a graceful degradation in the application if resources or services are unavailable. Understand what the client is expecting from the application, and create a design that allows for alternatives when a failure occurs.
-   Data/state availability. For consistent access to persistent data, use Windows Clustering to provide failover support.
-   Service availability. You can use Network Load Balancing to load balance incoming IP requests across a cluster of servers.

## Related topics

<dl> <dt>

[Designing for Deployment](designing-for-deployment.md)
</dt> <dt>

[Designing for Scalability](designing-for-scalability.md)
</dt> <dt>

[Designing for Security](designing-for-security.md)
</dt> </dl>

 

 



