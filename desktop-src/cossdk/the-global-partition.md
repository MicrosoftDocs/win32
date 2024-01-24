---
description: The Global Partition
ms.assetid: db11e6f5-0a3d-44ce-9a51-90d7e2b80981
title: The Global Partition
ms.topic: article
ms.date: 05/31/2018
---

# The Global Partition

In addition to administrator-defined partitions and partition sets, there is a special partition on each computer called a *global partition*. A global partition is automatically created when COM+ is installed. The global partition is designed to contain system-wide applications that need to be accessible to all users on a server or in the domain. Installing an application into the global partition removes the need to install a copy of the application into each individual user's partition set.

If a user's partition set does not include a specific application that the user is attempting to access, but that application is installed in the global partition, the application is activated from the global partition. In this case, however, all components of the application installed in the global partition must be marked as public, not private, components.

## Related topics

<dl> <dt>

[Default Partitions](default-partitions.md)
</dt> <dt>

[Local Partitions](local-partitions.md)
</dt> <dt>

[Partition Properties](partition-properties.md)
</dt> <dt>

[Partitions and Active Directory](partitions-and-active-directory.md)
</dt> </dl>

 

 



