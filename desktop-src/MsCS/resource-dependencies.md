---
title: Resource Dependencies
description: A dependent resource requires, or depends on, another resource to operate.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2ad913d2-99cb-4885-a1de-822f77dc2030'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource dependencies Failover Cluster", "resources Failover Cluster ,dependencies", "dependencies Failover Cluster"]
---

# Resource Dependencies

A dependent [resource](resources.md) requires, or depends on, another resource to operate. For example, if a [Generic Application](generic-application.md) resource requires access to shared physical storage; it would depend on a [Physical Disk](physical-disk.md) resource. The following terms describe resources in a dependency relationship:

-   A *dependent resource* depends on other resources (the dependencies).
-   A *dependency* is a resource on which another resource depends.
-   A *dependency hierarchy* is a series of dependency relationships such that resource A depends on resource B, resource B depends on resource C, and so on.

Resources in a dependency relationship obey the following rules:

-   A dependent resource and all of its dependencies must be in the same group.
-   The [Cluster service](cluster-service.md) takes a dependent resource offline before any of its dependencies are taken offline, and brings a dependent resource online after all its dependencies are online, as determined by the dependency hierarchy.

Some of the default [resource types](resource-types.md) have required dependencies, as summarized in the following table.



| Resource                                                                       | Required dependencies                                                                                                         |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| [DHCP Service](dhcp-service.md)                                               | [Physical Disk](physical-disk.md) resource                                                                                   |
| [Distributed Transaction Coordinator](distributed-transaction-coordinator.md) | [Network Name](network-name.md) resource, Physical Disk resource                                                             |
| [File Share](file-share.md)                                                   | None                                                                                                                          |
| [Generic Application](generic-application.md)                                 | None                                                                                                                          |
| [Generic Service](generic-service.md)                                         | None                                                                                                                          |
| [IP Address](ip-address.md)                                                   | None                                                                                                                          |
| Message Queuing (MSMQ)                                                         | [IP Address](ip-address.md) resource, [Network Name](network-name.md) resource, [Physical Disk](physical-disk.md) resource |
| [Network Name](network-name.md)                                               | [IP Address](ip-address.md) resource                                                                                         |
| [Physical Disk](physical-disk.md)                                             | None                                                                                                                          |
| [Print Spooler](print-spooler.md)                                             | [Network Name](network-name.md) resource, [Physical Disk](physical-disk.md) resource                                        |
| [WINS Service](wins-service.md)                                               | [Physical Disk](physical-disk.md) resource                                                                                   |



 

 

 




