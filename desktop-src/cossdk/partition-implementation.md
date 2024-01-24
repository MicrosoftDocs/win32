---
description: When installed on an application server, COM+ automatically creates a partition, known as the global partition.
ms.assetid: fbe894ae-5356-4522-884a-dc579a3a8dd3
title: Partition Implementation
ms.topic: article
ms.date: 05/31/2018
---

# Partition Implementation

When installed on an application server, COM+ automatically creates a partition, known as the *global partition*. The global partition includes a standard set of COM+ applications. COM+ applications that are installed in the global partition are automatically available to all users on the server. If you have other COM+ applications that you would like to make available to all users on the server, you can add them into the global partition.

In addition to the global partition, you can create other partitions for users on that server only, or for users throughout the domain. Creating additional partitions and installing multiple configurations of a COM+ application into them allows your users to execute those application configurations simultaneously on the same computer. Also, by installing COM+ applications into a partition other than the global partition, you can control user access to those applications.

**Windows XP:** The ability to create, configure, or delegate COM+ partitions is not available. The global partition is the only COM+ partition available.

For more information on local partitions and partitions defined within Active Directory, see the following topics:

-   [Local Partitions](local-partitions.md)
-   [Partitions and Active Directory](partitions-and-active-directory.md)
-   [Default Partitions](default-partitions.md)
-   [The Global Partition](the-global-partition.md)
-   [Partition Properties](partition-properties.md)

## Related topics

<dl> <dt>

[Application Design Restrictions](application-design-restrictions.md)
</dt> <dt>

[COM+ Queued Components and Partitions](com--queued-components-and-partitions.md)
</dt> <dt>

[Registering and Activating Components in Partitions](registering-and-activating-components-in-partitions.md)
</dt> <dt>

[What Are COM+ Partitions?](what-are-com--partitions-.md)
</dt> </dl>

 

 



