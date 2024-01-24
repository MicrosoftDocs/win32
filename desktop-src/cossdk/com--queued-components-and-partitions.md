---
description: The COM+ queued components service fully supports the concept of partitions. That is, when a queued component within a partition is executed, the message is queued and the component is eventually executed within the components partition.
ms.assetid: 08b0f7b5-6c45-4471-9634-1f42fbbf500c
title: COM+ Queued Components and Partitions
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Queued Components and Partitions

The COM+ queued components service fully supports the concept of partitions. That is, when a queued component within a partition is executed, the message is queued and the component is eventually executed within the component's partition.

## Queue Names for Partitioned Components

Traditionally, the queued components service uses the application name as the queue name. This means that in a non-partitions scenario, where only one instance of an application name exists on a computer, each application name has its own message queue.

In the case of partitions, however, where multiple instances of the same application name can exist on a computer, the queued components service uses the same queue for any queued components that share the same application name.

## Activating Queued Components

The same rules for how the partition ID is used to activate a non-queued component applies to a queued component, as follows:

-   If a moniker is used to activate the queued component and a partition ID is included, this partition ID is used to locate the partition. This partition ID takes precedence over any partition ID that might exist in the context for the component being activated.
-   If no moniker is being used to activate the component, the partition ID that is in the object's context is used.
-   If no partition ID exists in the object's context, the default user-to-partition mapping within Active Directory is used.

> [!Note]  
> If a server computer is disconnected from the network and if the user-to-partition set mapping is changed while the server is disconnected, the partition cache might contain outdated user-to-partition set mapping. This could result in an activation error if user-to-partition set mapping is the mechanism used to activate a component.

 

COM+ events are fully integrated into partitions. This means that a subscriber can subscribe to a publisher whose application resides within a partition. To allow this subscription, the subscriber class collection includes two partition-related properties—an event class partition ID and an event class application ID.

## Related topics

<dl> <dt>

[Application Design Restrictions](application-design-restrictions.md)
</dt> <dt>

[Partition Implementation](partition-implementation.md)
</dt> <dt>

[Registering and Activating Components in Partitions](registering-and-activating-components-in-partitions.md)
</dt> <dt>

[What Are COM+ Partitions?](what-are-com--partitions-.md)
</dt> </dl>

 

 



