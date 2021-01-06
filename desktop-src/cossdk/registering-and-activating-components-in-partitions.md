---
description: Registering and Activating Components in Partitions
ms.assetid: 2cca71da-c7f7-4997-b63a-74ba266e9e95
title: Registering and Activating Components in Partitions
ms.topic: article
ms.date: 05/31/2018
---

# Registering and Activating Components in Partitions

After a partition has been created, the next step is register your COM+ components within that partition. A component is registered within a partition when a new COM+ application is created or when an existing COM+ application is installed into the partition. To ease the administration of registration when multiple partitions contain the same COM+ components, the partitions service allows an administrator to copy applications or components from one partition into another. When a COM+ application or a component is copied, all associated partition properties are copied with it, except the application's identity or any of the members of a role.

When the client program calls the [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance) or [**CoGetObject**](/windows/desktop/api/objbase/nf-objbase-cogetobject) function to instantiate an object, COM+ performs two distinct steps, as follows:

1.  Locates the partition in which the component resides
2.  Locates the correct component within that partition

The following topics in this section describe these steps in detail:

-   [Locating Partitions During Activation](locating-partitions-during-activation.md)
-   [Locating a Component for Activation](locating-a-component-for-activation.md)

## Related topics

<dl> <dt>

[Application Design Restrictions](application-design-restrictions.md)
</dt> <dt>

[COM+ Queued Components and Partitions](com--queued-components-and-partitions.md)
</dt> <dt>

[Partition Implementation](partition-implementation.md)
</dt> <dt>

[What Are COM+ Partitions?](what-are-com--partitions-.md)
</dt> </dl>

 

 
