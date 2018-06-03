---
title: Direct Connections
description: You can connect directly to a specific node in the cluster by specifying an object path that resolves to the node's dedicated IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f1dd33b-42f4-482f-9445-08eb8f24cdaa
ms.prod: windows-server-dev
ms.technology:
- network-load-balancing
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- connections Failover Cluster ,direct NLB connections
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Direct Connections

You can connect directly to a specific [*node*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-5-gly) in the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly) by specifying an object path that resolves to the node's dedicated IP address. Direct connections offer several advantages:

-   The connection will succeed unless [*WMI*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-21-gly) cannot establish a network connection to the node based on the [*namespace*](https://msdn.microsoft.com/library/aa371764#mscs-n---z-1-gly). Network Load Balancing does not have to be running on the node.
-   You can configure the [*cluster IP address*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-6-gly) of the node without affecting your connection.
-   You can target configuration operations more effectively.

Node-specific object paths have the form:

**\\\\***name***\\root\\MicrosoftNLB**

where *name* can be any name or IP address that resolves to the dedicated IP address of a node.

 

 




