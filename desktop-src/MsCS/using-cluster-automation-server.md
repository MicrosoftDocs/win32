---
title: Using the Failover Cluster Automation Server
description: You can use the Failover Cluster Automation Server APIs to manage or administer failover clusters remotely through scripting languages.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 958dee2a-13e2-433f-b314-d62d1eb7183e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Failover Cluster APIs Failover Cluster ,using Failover Cluster Automation Server
- Windows Failover Clustering Failover Cluster ,Failover Cluster APIs,using Failover Cluster Automation Server
- Failover Cluster Automation Server Failover Cluster ,using
- Failover Cluster APIs Failover Cluster ,using Cluster Automation Server
- Windows Clustering Failover Cluster ,Failover Cluster APIs,using Cluster Automation Server
- Cluster Automation Server Failover Cluster ,using
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the Failover Cluster Automation Server

\[The [Failover Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) is available for use in Windows Server 2008. It may be altered or unavailable in subsequent versions.\]

You can use the Failover Cluster Automation Server APIs to manage or administer failover clusters remotely through scripting languages. Here are the basic steps to implement the Failover Cluster Automation Server APIs:

1.  Create a Failover Cluster Automation Server Script. For an example, see [Creating a Failover Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).
2.  Use the topic [Failover Cluster Automation Server Object Hierarchy](object-hierarchy.md) to locate the objects that can perform your cluster operations.
3.  In your script, retrieve the objects and then invoke the properties and methods that perform your cluster operations. For reference information, see [Failover Cluster Automation Server Reference](cluster-automation-server-reference.md). For examples, see the next section.

### Examples

The following code examples demonstrate how to create scripts for the Failover Cluster Automation Server:

-   [Creating a Failover Cluster Automation Server Script](creating-a-cluster-automation-server-script.md)
-   [Enumerating Objects with the Failover Cluster Automation Server](enumerating-objects-with-cluster-automation-server.md)
-   [Creating Cluster Objects with the Failover Cluster Automation Server](creating-cluster-objects-with-cluster-automation-server.md)
-   [Configuring Resources with the Failover Cluster Automation Server](configuring-resources-with-cluster-automation-server.md)

## Related topics

<dl> <dt>

[Using the Failover Cluster APIs](using-the-server-cluster-api.md)
</dt> <dt>

[Failover Cluster Automation Server Reference](cluster-automation-server-reference.md)
</dt> </dl>

 

 




