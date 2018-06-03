---
title: Failover Cluster Utility Functions
description: The failover cluster utility functions support a wide range of functionality, from general purpose helper functions to thread and service management functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 867044a6-b3ad-45b9-8dc4-48529a3e6e94
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- failover cluster utility functions Failover Cluster
- utility functions Failover Cluster
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Utility Functions

The failover cluster utility functions support a wide range of functionality, from general purpose helper functions to thread and service management functions. Both [*cluster-aware applications*](https://www.bing.com/search?q=*cluster-aware applications*) and [resource DLLs](resource-dlls.md) can use the failover cluster utility functions. However, some utility functions are intended only for use by resource DLLs. Cluster-aware applications should follow the topic [standard order of preference](standard-order-of-preference.md) before using utility functions intended for resource DLLs.

Most of the utility functions are part of the [Resource API](resource-api.md). The only exceptions are the backup and restore functions, which are part of the [Failover Cluster API](cluster-api.md).

## In this section

<dl> <dt>

[Health Fault Utility Functions](health-fault-utility-functions.md)
</dt> <dd>

The health fault utility functions.

</dd> <dt>

[Backup and Restore Functions](backup-and-restore-functions.md)
</dt> <dd>

The backup and restore functions are used by applications to take snapshots of the current [cluster](https://www.bing.com/search?q=cluster) configuration and restore those configurations at a later time.

</dd> <dt>

[Cryptography Functions](cryptography-functions.md)
</dt> <dd>

Cryptography functions are used by applications to manage [Checkpointing](checkpointing.md) data for cluster resources.

</dd> <dt>

[General Utility Functions](general-utility-functions.md)
</dt> <dd>

The general utility functions are used by applications and [resource DLLs](resource-dlls.md) to perform common tasks such as duplicating strings and validating paths.

</dd> <dt>

[Property List Parsing Functions](property-list-parsing-functions.md)
</dt> <dd>

The [property list](property-lists.md) parsing functions are used by applications and [resource DLLs](resource-dlls.md) to locate specific values or properties in a property list.

</dd> <dt>

[Property Structure Construction Functions](property-structure-construction-functions.md)
</dt> <dd>

The property structure construction functions are used by applications and [resource DLLs](resource-dlls.md) to build [property lists](property-lists.md), [parameter blocks](parameter-blocks.md), and [property tables](property-tables.md).

</dd> <dt>

[Resource Utility Functions](resource-utility-functions.md)
</dt> <dd>

The resource utility functions allow applications and [resource DLLs](resource-dlls.md) to manage multiple [cluster resources](resources.md).

</dd> <dt>

[Service Utility Functions](service-utility-functions.md)
</dt> <dd>

The [service](https://www.bing.com/search?q=service) utility functions manage services for [resource DLLs](resource-dlls.md).

</dd> <dt>

[Thread Management Utility Functions](thread-management-utility-functions.md)
</dt> <dd>

The thread management utility functions manage worker threads for [resource DLLs](resource-dlls.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> </dl>

 

 




